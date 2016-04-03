%   Samuel Gluss
%   CS840 project 3 PLOC/LLOC and Cyclomatic Complexity
%   3-26-2016

%   get working directory for project
wd = fileparts(mfilename('fullpath'));
wd = [wd '\..\'];

%   get data from cppParse and BM outfiles
data = dlmread([wd 'outfile.txt']);
%   sort rows of outfile by file number
data = sortrows(data);

%   create dataClass array
dataClasses = DataSet.empty();
for i = 1:size(data,1)
    dataClasses(i) = DataSet(data(i,:));
end

%   project4 LLOC vs V
LLOCV([dataClasses.cyclomaticComplexity], [dataClasses.LLOC])
VLLOCTable([dataClasses.cyclomaticComplexity], [dataClasses.LLOC])