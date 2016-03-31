% Compares the LLOC data from Benchmaker and CPPparse
function [  ] = LLOCCompare( dataClasses )
    figure('Position', [0, 0, 1280, 720]);
    h = plot([dataClasses.BMspecPLOC], [[dataClasses.LLOC];...
        [dataClasses.BMactualLLOC]]');
    %   configure axis limits and stepsize
    ax = gca;
    ax.XTick = dataClasses(1).BMspecPLOC:dataClasses(3).BMspecPLOC-dataClasses(1).BMspecPLOC:dataClasses(end).BMspecPLOC;
    ax.XLim = [dataClasses(1).BMspecPLOC dataClasses(end).BMspecPLOC];
    %   set title, labels and legend
    title('Benchmaker VS Test Parser: LLOC Count');
    ylabel('Measured LLOC');
    xlabel('PLOC');
    legend(h,'Test Parser','Benchmaker',...
        'Location','northwest');

    %   outputing data to disk
    wd = fileparts(mfilename('fullpath'));
    figDir = [wd '\..\figures\'];
    set(gcf,'PaperUnits','inches','PaperPosition',[0 0 12 7])
    print([figDir 'BMvParserLLOC'],'-dpng','');
end