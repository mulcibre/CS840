function [  ] = bestWorstAndQfactor( object, matSizes, opLabels )

%   create figure with size 1280x720
figure('Position', [0, 0, 1280, 720]);
subplot(1,2,1);
plot(matSizes, [object.rawData(object.indexOfWorst,:);...
    object.rawData(object.indexOfBest,:)]');
%   configure axis limits and stepsize
ax = gca;
ax.XTick = 20:40:500;
ax.XLim = [20 500];
%   set title, labels and legend
title(['Fastest and Slowest Matrix Multiplication in ' object.title]);
ylabel('Time (s)');
xlabel('Matrix Size (NxN)');
legend([opLabels(object.indexOfWorst) opLabels(object.indexOfBest)],...
    'Location','northwest');

subplot(1,2,2);
plot(matSizes, cell2mat({object.QFactorArr}'));
ax = gca;
ax.XTick = 20:40:500;
ax.XLim = [20 500];
title(['Q factors for Matrix Multiplication in ' object.title]);
ylabel('Q factor (% speedup)');
xlabel('Matrix Size (NxN)');

%   outputing data to disk
wd = fileparts(mfilename('fullpath'));
set(gcf,'PaperUnits','inches','PaperPosition',[0 0 14 9])
print([wd '\figures\' object.title 'bestworstQfactor'],'-dpng','');
end