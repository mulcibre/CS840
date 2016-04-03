function [  ] = VLLOCTable( VData, LLOCData )
%   This function will use a dataset and opslabels
%   to output a table with useful data

labelFontSizeIncrease = 2;
%   Generate the HTML injection string
htmlFSInc = strcat(['<html><font size=+' num2str(labelFontSizeIncrease) '>']);

V = cell2mat({VData})';
LLOC = cell2mat({LLOCData})';

data = horzcat(LLOC, V)';

%   row names
rNames = {'Plateau';'Parabolic Approximation';'Array Processing';...
    'Big Integers';'Iteration vs. Recursion';'Matrix Multiplication';...
    'QuickSort';'Matrix Inversion'}';

%   column labels
cNames = {'LLOC';'V'};

%   This is a silly trick I learned on the internet
%   HTML injection works in MatLab
cNames = strcat(htmlFSInc,cNames);
rNames = strcat(htmlFSInc,rNames);

f = figure('Position', [0, 0, 1280, 720]);
t = uitable(f,'Data',data',...
    'ColumnName',cNames,...
    'RowName',rNames,...
    'FontSize',18);
% Set width and height
t.Position(3) = t.Extent(3);
t.Position(4) = t.Extent(4);

%   Change figure dimensions so table can be saved correctly
f.Position(3) = t.Extent(3)+20;
f.Position(4) = t.Extent(4)+20;

%   The below code requires the findjobj function
%   download it here: http://www.mathworks.com/matlabcentral/fileexchange/14317-findjobj-find-java-handles-of-matlab-graphic-objects
jscrollpane = findjobj(t);
jTable = jscrollpane.getViewport.getView;

cellStyle = jTable.getCellStyleAt(0,0);
cellStyle.setHorizontalAlignment(cellStyle.CENTER);

% Table must be redrawn for the change to take affect
jTable.repaint;

%   outputing data to disk
    %   get pixels per inch, for scaling conversion
    pixperinch = get(0,'ScreenPixelsPerInch');
    %   get output directory
    wd = fileparts(mfilename('fullpath'));
    figDir = [wd '\..\figures\tables\'];
    %   dimensions must account for figure position
    set(gcf,'PaperUnits','inches','PaperPosition',...
        [0 0 (t.Extent(3)+t.Position(1))/pixperinch (t.Extent(4)+t.Position(2))/pixperinch])
    
    %   output will still have margins on left and bottom, these must be
    %   trimmed
    print([figDir 'LLOCVTable'],'-dpng','');
end