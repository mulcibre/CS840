%   Samuel Gluss
%   CS840 project 3 PLOC/LLOC and Cyclomatic Complexity
%   3-26-2016

%   get working directory for project
wd = fileparts(mfilename('fullpath'));
wd = [wd '\..\'];

%   get data from cppParse and BM outfiles
data = dlmread([wd 'outfile.txt']);
BMout = dlmread([wd 'benchmaker\' 'cleanBM1out.txt']);
sizeTimeData = dlmread([wd 'benchmaker\' 'compilerTestOutfile.txt']);
%   sort rows of outfiles by benchmark
data = sortrows(data);
sizeTimeData = sortrows(sizeTimeData);

data = horzcat(data, BMout, sizeTimeData(:,2:end));

%   create dataClass array
dataClasses = BMDataSet.empty();
for i = 1:size(data,1)
    dataClasses(i) = BMDataSet(data(i,:));
end

LLOCCompare(dataClasses);

%   get data from cppParse and BM outfiles
cs600data = dlmread([wd 'othercpp\' 'outfile.txt']);
BMout = zeros(size(cs600data,1),4);
sizeTimeData = dlmread([wd 'othercpp\' 'compilerTestOutfile.txt']);
sizeTimeData = sortrows(sizeTimeData);
cs600data = horzcat(cs600data, BMout, sizeTimeData(:,2:end));

%   create cs600 dataClass array
cs600dataClasses = BMDataSet.empty();
for i = 1:size(cs600data,1)
    cs600dataClasses(i) = BMDataSet(cs600data(i,:));
end

% %part 3 comparisons: LLOC, PLOC, and executable size
% LLOCvMcoeff = plotCompilerData([dataClasses.LLOC],[dataClasses.sizeofEXE],...
%     'Test Parser: LLOC vs program size','Measured LLOC','EXE size (bytes)','LLOCvsCompiledSize');
% PLOCvMcoeff = plotCompilerData([dataClasses.PLOC],[dataClasses.sizeofEXE],...
%     'Test Parser: PLOC vs program size','Measured PLOC','EXE size (bytes)','PLOCvsCompiledSize');
% PLOCvLLOCcoeff = plotCompilerData([dataClasses.PLOC],[dataClasses.LLOC],...
%     'Test Parser: PLOC vs LLOC','Measured PLOC','Measured LLOC','PLOCvsLLOC');

%part 4 comparisons: LLOC, PLOC, and executable size with CS600 code
% compareCompilerData([cs600dataClasses.LLOC],[cs600dataClasses.sizeofEXE],...
%      'Test Parser: LLOC vs program size','Measured LLOC','EXE size (bytes)','cs600LLOCvsCompiledSize',LLOCvMcoeff);
% compareCompilerData([cs600dataClasses.PLOC],[cs600dataClasses.sizeofEXE],...
%      'Test Parser: PLOC vs program size','Measured PLOC','EXE size (bytes)','cs600PLOCvsCompiledSize',PLOCvMcoeff);
% compareCompilerData([cs600dataClasses.PLOC],[cs600dataClasses.LLOC],...
%      'Test Parser: PLOC vs LLOC','Measured PLOC','Measured LLOC','cs600PLOCvsLLOC',PLOCvLLOCcoeff);

%part 5 compile time VS. LLOC
compileTimeLLOCmodel([dataClasses.compileTime], [dataClasses.LLOC]);

%project4 LLOC vs V
%LLOCV([cs600dataClasses.cyclomaticComplexity], [cs600dataClasses.LLOC])
%VLLOCTable([cs600dataClasses.cyclomaticComplexity], [cs600dataClasses.LLOC])