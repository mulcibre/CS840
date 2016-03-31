%   Compares raw data and best fit line to another best fit line
function [] = compareCompilerData(otherData1, otherData2, titleSet, xlabelSet, ylabelSet,fn, BMcoeff)
    figure('Position', [0, 0, 1280, 720]);
    x1 = otherData1;
    y1 = otherData2;
    
    %   linear fit data
    coeffs = polyfit(x1, y1, 1);
    % Get fitted values
    domainSize = x1(end) - x1(1);
    fittedX = [x1(1)-domainSize, x1(end)+domainSize];
    fittedY = polyval(coeffs, fittedX);
    BMfittedy = polyval(BMcoeff, fittedX);
    
    h = plot(fittedX, [fittedY; BMfittedy]);
    hold on
    plot(x1,y1,'Ob');
    %   change y axis tick exponent
    ax = gca;
    ax.YAxis.Exponent = 0;
    
    %   set title, labels and legend
    title(titleSet);
    ylabel(ylabelSet);
    xlabel(xlabelSet);
    legend(h,['Best Fit line y = ' num2str(coeffs(1)) 'x + ' num2str(coeffs(2))],...
        ['BM data Fit line y = ' num2str(BMcoeff(1)) 'x + ' num2str(BMcoeff(2))],...
        'Location','northwest');
    
    %rescale figure
    domainSize = max(x1) - min(x1);
    rangeSize = max(y1) - min(y1);
    extraSpace = 0.50;
    axis([min(x1) - domainSize * extraSpace,max(x1)+ domainSize * extraSpace,...
        min(y1)- rangeSize * extraSpace,max(y1)+ rangeSize * extraSpace])
    
    %   outputing data to disk
    wd = fileparts(mfilename('fullpath'));
    figDir = [wd '\..\figures\'];
    set(gcf,'PaperUnits','inches','PaperPosition',[0 0 12 7])
    print([figDir fn],'-dpng','');
end