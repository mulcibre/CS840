%   Samuel Gluss
%   CS840 project 2 matrix multiplication in different languages
%   3-8-2016

%   this script must be located in the project base directory to work
%   get working directory for project
wd = fileparts(mfilename('fullpath'));
%   get outfile directory
dataDir = [wd '\outfiles\test0\'];
procDataDir = [wd '\outfiles\3-13-2016 100min\'];
cppreleaseDir = [wd '\outfiles\cpprelease\'];
opLabelsDir = [wd '\createLabels\'];

%   read delimited data files into matrices
javaData = dlmread([procDataDir 'javaoutfile.txt']);
cppDebugData = dlmread([procDataDir 'c++outfile.txt']);
cppRelData = dlmread([cppreleaseDir 'c++outfile.txt']);
rubyData = dlmread([dataDir 'Rubyoutfile.txt']);
jsData = dlmread([dataDir 'JSoutfile.txt']);
pythonData = dlmread([dataDir 'Pythonoutfile.txt']);

% put data sets into objects with names
classJavaData = dataSet('Java', javaData);
classCppDebugData = dataSet('C++ Debug Mode', cppDebugData);
classCppRelData = dataSet('C++ Release Mode', cppRelData);
classRubyData = dataSet('Ruby', rubyData);
classJSData = dataSet('JS', jsData);
classPythonData = dataSet('Python', pythonData);

objects = [classJavaData 
           classCppDebugData
           classCppRelData
           classRubyData 
           classJSData
           classPythonData];

%   open text file with label data, read into array
labelsFile = fopen([opLabelsDir 'labels.txt']);
opLabels = textscan(labelsFile,'%s','Delimiter',',');
%   weird matlab behaviour, have to store opLabels as temp
opLabels = opLabels{1};

%   plotting data
%   X-axis - 20 to 500 inclusive, step size of 20
matSizes = 20:20:500;

%   plotting all data gathered for one language
figure
object = classCppRelData;
plot(matSizes, object.rawData');
ax = gca;
ax.XTick = 20:40:500;
ax.XLim = [20 500];
title(strcat(object.title, ' Matrix Multiplication'));
    ylabel('Time (s)');
    xlabel('Matrix Size (NxN)');

    %   showing Q Factor Curves for each language together
figure
plot(matSizes, cell2mat({objects.QFactorArr}'));
title('Q factors for Matrix Multiplication');
    ylabel('Q factor (% speedup)');
    xlabel('Matrix Size (NxN)');
    legend({objects.title}');

    %   uitable for displaying data comparison
    makeUITable(objects,opLabels);
    
    %   side by side display of best/worst data and Qfactor
    for i = 1:length(objects)
        bestWorstAndQfactor(objects(i),matSizes, opLabels)
    end
    
%   closing all files
fclose all;
