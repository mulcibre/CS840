function [rowMeanRank] = createRankings(dataSet)
    [rows, columns, ] = size(dataSet);
    
    %retMat(1:rows,1:columns,2) = 0;
    rankings(1:rows,1:columns) = 0;
    rowRank(1:rows,1:columns) = 0;
    [B, rankings] = sort(dataSet);
    rowMeanRank(1:columns) = 0;
    
    for row = 1 : rows
        for col = 1 : columns 
            rowRank(rankings(row,col),col) = row;
        end
    end
        for row = 1 : rows 
            rowMeanRank(row) = mean(rowRank(row,:));
        end
end