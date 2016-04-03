classdef DataSet
    properties
        runNum
        commas
        equals
        ifCount
        forCount
        whileCount
        semiCount
        switchCount
        caseCount
        ANDCount
        ORCount
        PLOC
        LLOC
        cyclomaticComplexity
    end
    
    methods
        % methods, including the constructor are defined in this block
        function obj = DataSet(data)
            obj.runNum = data(1);
            obj.commas = data(2);
            obj.equals = data(3);
            obj.ifCount = data(4);
            obj.forCount = data(5);
            obj.whileCount = data(6);
            obj.semiCount = data(7);
            obj.switchCount = data(8);
            obj.caseCount = data(9);
            obj.ANDCount = data(10);
            obj.ORCount = data(11);
            obj.PLOC = data(12);
            obj.LLOC = data(13);
            obj.cyclomaticComplexity = data(14);
        end
    end
end