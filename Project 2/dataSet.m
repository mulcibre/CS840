classdef dataSet
    properties
        title
        rawData
        fastestData
        slowestData
        indexOfBest
        indexOfWorst
        QFactorArr
        QFactor
    end
    
    methods
       % methods, including the constructor are defined in this block
       function obj = dataSet(a, b)
           obj.title = a;
           obj.rawData = b;
           %    set data for fastest and slowest
           for col = 1 : size(obj.rawData,2)
               obj.fastestData(col) = min(obj.rawData(:,col));
               obj.slowestData(col) = max(obj.rawData(:,col));
               QFactor = (100 * (obj.slowestData(col) - obj.fastestData(col))) / (obj.slowestData(col) + obj.fastestData(col));
               obj.QFactorArr(col) = QFactor;
           end
           obj.QFactor = mean(obj.QFactorArr);
           %    get indices of data which was fastest/slowest for final
           %    matrix multiplication op
            [~,obj.indexOfBest] = min(obj.rawData(:,size(obj.rawData,2)));
            [~,obj.indexOfWorst] = max(obj.rawData(:,size(obj.rawData,2)));   
       end
    end
end