function [] = LLOCV(VData, LLOCData)
    xdata = LLOCData;
    ydata = VData;
    
    %   linear fit data
    coeffs = polyfit(xdata, ydata, 1);
    % Get fitted values
    fittedY = polyval(coeffs, xdata);
    
    figure('Position', [0, 0, 1280, 720]);
    h = plot(xdata, [ydata; fittedY], 'O');
    
    %   change y axis tick exponent
    ax = gca;
    ax.YAxis.Exponent = 0;
    %   set title, labels and legend
    title('Relationship between LLOC and Cyclomatic Complexity');
    ylabel('Cyclomatic Complexity V');
    xlabel('LLOC');
    legend(h,'Raw Data',['Best Fit line y = ' num2str(coeffs(1)) 'x + ' num2str(coeffs(2))],...
        'Location','northwest');
    
    %add regression line
    hold on
    h = plot(xdata, fittedY, '-');
    
    %rescale figure
    domainSize = max(xdata) - min(xdata);
    rangeSize = max(ydata) - min(ydata);
    axis([min(xdata) - domainSize * .1,max(xdata)+ domainSize * .1,...
        min(ydata)- rangeSize * .1,max(ydata)+ rangeSize * .1])
    
    %   outputing data to disk
    wd = fileparts(mfilename('fullpath'));
    figDir = [wd '\..\figures\'];
    set(gcf,'PaperUnits','inches','PaperPosition',[0 0 12 7])
    print([figDir 'LLOCV'],'-dpng','');
end