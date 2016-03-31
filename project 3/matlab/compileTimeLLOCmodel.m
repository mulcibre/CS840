function [] = compileTimeLLOCmodel(times, LLOC)
    xdata = LLOC;
    ydata = times;
    
    %   compute coefficients and generate best fit curve
    f = @(x,xdata)x(1)+x(2)*xdata.^x(3);
    x = lsqcurvefit(f,[1,1,1],xdata,ydata);
    yfitData = f(x,xdata);
    
    %   plot data and fit curve
    figure('Position', [0, 0, 1280, 720]);
    h = plot(xdata, [ydata; yfitData]);

    %   change y axis tick exponent
    ax = gca;
    ax.YAxis.Exponent = 0;
    
    %   set title, labels and legend
    title(['LLOC VS Compile Time and Best Fit Curve T = ' num2str(x(1)) ' + ' num2str(x(2)) '*(LLOC)^{' num2str(x(3)) '}']);
    ylabel('Compile Time (s)');
    xlabel('LLOC');
    legend(h,'Raw Data','Best Fit line',...
        'Location','northwest');
    
    %   outputing data to disk
    wd = fileparts(mfilename('fullpath'));
    figDir = [wd '\..\figures\'];
    set(gcf,'PaperUnits','inches','PaperPosition',[0 0 12 7])
    print([figDir 'compiletimeVSLLOC'],'-dpng','');
    
end