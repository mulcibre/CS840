function [  ] = VLLOCTable( VData, LLOCData )
%   This function will use a dataset and opslabels
%   to output a table with useful data

labelFontSizeIncrease = 2;
%   Generate the HTML injection string
htmlFSInc = strcat(['<html><font size=+' num2str(labelFontSizeIncrease) '>']);

V = cell2mat({VData})';
LLOC = cell2mat({LLOCData})';

data = horzcat(V, LLOC)';

%   row names
rNames = {'program1';'program2';'program3';'program4';'program5'}';

%   column labels
cNames = {  'V';'LLOC'};

%   This is a silly trick I learned on the internet
%   HTML injection works in MatLab
cNames = strcat(htmlFSInc,cNames);
rNames = strcat(htmlFSInc,rNames);

f = figure;
t = uitable(f,'Data',data',...
    'ColumnName',cNames,...
    'RowName',rNames,...
    'FontSize',18);
% Set width and height
t.Position(3) = t.Extent(3);
t.Position(4) = t.Extent(4);

%   The below code requires the findjobj function
%   download it here: http://www.mathworks.com/matlabcentral/fileexchange/14317-findjobj-find-java-handles-of-matlab-graphic-objects
jscrollpane = findjobj(t);
jTable = jscrollpane.getViewport.getView;

cellStyle = jTable.getCellStyleAt(0,0);
cellStyle.setHorizontalAlignment(cellStyle.CENTER);

% Table must be redrawn for the change to take affect
jTable.repaint;

end