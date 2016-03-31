function [coeffs] = plotCompilerData(dataClass1,dataClass2, titleSet, xlabelSet, ylabelSet,fn)
    
    x = dataClass1;
    y = dataClass2;
    
    %   linear fit data
    coeffs = polyfit(x, y, 1);
    % Get fitted values
    fittedY = polyval(coeffs, x);
    
    figure('Position', [0, 0, 1280, 720]);
    h = plot(x, [y; fittedY]);

    %   change y axis tick exponent
    ax = gca;
    ax.YAxis.Exponent = 0;
    
    %   set title, labels and legend
    title(titleSet);
    ylabel(ylabelSet);
    xlabel(xlabelSet);
    legend(h,'Raw Data',['Best Fit line y = ' num2str(coeffs(1)) 'x + ' num2str(coeffs(2))],...
        'Location','northwest');
    
    %   outputing data to disk
    wd = fileparts(mfilename('fullpath'));
    figDir = [wd '\..\figures\'];
    set(gcf,'PaperUnits','inches','PaperPosition',[0 0 12 7])
    print([figDir fn],'-dpng','');
end