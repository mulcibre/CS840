function [] = compilerCompare()
    %   All results from compiled program execution tests
    VSMMDebugTime = 0.533731;
    VSMMReleaseTime = 0.0985869;
    VSQSDebugTime = 1.7019;
    VSQSReleaseTime = 0.800633;
    GCCMMDebugTime = 0.543301;
    GCCMMReleaseTime = 0.0965004;
    GCCQSDebugTime = 1.55041;
    GCCQSReleaseTime = 0.970503;
    
    %   Lenovo Thinkpad T420s
    %   windows 7 pro SP1
    %   Intel Core i5-2540m @ 2.6Ghz
    %   16gb RAM
    T420VSMMDebugTime = 0.619233;
    T420VSMMReleaseTime = 0.136393;
    T420VSQSDebugTime = 1.79803;
    T420VSQSReleaseTime = 0.866327;
    T420GCCMMDebugTime = 0.614641;
    T420GCCMMReleaseTime = 0.12636;
    T420GCCQSDebugTime = 1.89384;
    T420GCCQSReleaseTime = 1.23864;
    
    %   create barplot
    figure('Position', [0, 0, 1280, 720]);
    subplot(2,1,1);
    %   initialize plot with W541 Data
    bar([VSMMDebugTime,VSMMReleaseTime,VSQSDebugTime,VSQSReleaseTime,...
        GCCMMDebugTime,GCCMMReleaseTime,GCCQSDebugTime,GCCQSReleaseTime],'g');   
    %      Set labels for bars 
    set(gca,'xticklabel',{'VSMMDebug';'VSMMRelease';'VSQSDebug';'VSQSRelease';...
        'GCCMMDebug';'GCCMMRelease';'GCCQSDebug';'GCCQSRelease'});
     title('Executable Runtimes for W541');
    ylabel('Runtime (s)');
    
    subplot(2,1,2);
    %   initialize plot with T420 Data
    bar([T420VSMMDebugTime,T420VSMMReleaseTime,T420VSQSDebugTime,T420VSQSReleaseTime,...
        T420GCCMMDebugTime,T420GCCMMReleaseTime,T420GCCQSDebugTime,T420GCCQSReleaseTime],'g');
    %      Set labels for bars 
    set(gca,'xticklabel',{'VSMMDebug';'VSMMRelease';'VSQSDebug';'VSQSRelease';...
        'GCCMMDebug';'GCCMMRelease';'GCCQSDebug';'GCCQSRelease'});
     title('Executable Runtimes for T420s');
    ylabel('Runtime (s)');
    
    %   get ratios of performance between compilers
    MMDebugRatio = VSMMDebugTime / GCCMMDebugTime;
    MMReleaseRatio = VSMMReleaseTime / GCCMMReleaseTime;
    QSDebugRatio = VSQSDebugTime / GCCQSDebugTime;
    QSReleaseRatio = VSQSReleaseTime / GCCQSReleaseTime;
    T420MMDebugRatio = T420VSMMDebugTime / T420GCCMMDebugTime;
    T420MMReleaseRatio = T420VSMMReleaseTime / T420GCCMMReleaseTime;
    T420QSDebugRatio = T420VSQSDebugTime / T420GCCQSDebugTime;
    T420QSReleaseRatio = T420VSQSReleaseTime / T420GCCQSReleaseTime;
    
    %   get ratios of performance between w541 and T420s
    VSMMDebugRatio = VSMMDebugTime / T420VSMMDebugTime;
    VSMMReleaseRatio = VSMMReleaseTime / T420VSMMReleaseTime;
    VSQSDebugRatio = VSQSDebugTime / T420VSQSDebugTime;
    VSQSReleaseRatio = VSQSReleaseTime / T420VSQSReleaseTime;
    GCCMMDebugRatio = GCCMMDebugTime / T420GCCMMDebugTime;
    GCCMMReleaseRatio = GCCMMReleaseTime / T420GCCMMReleaseTime;
    GCCQSDebugRatio = GCCQSDebugTime / T420GCCQSDebugTime;
    GCCQSReleaseRatio = GCCQSReleaseTime / T420GCCQSReleaseTime;
    
    %   calculate geometric mean of performance ratio between compilers
    %   VC++ and GCC
    MMperfGeoMean = MMDebugRatio*MMReleaseRatio*T420MMDebugRatio*T420MMReleaseRatio;
    QSperfGeoMean = QSDebugRatio*QSReleaseRatio*T420QSDebugRatio*T420QSReleaseRatio;
    perfGeoMean = (MMperfGeoMean * QSperfGeoMean)^(1/8);
    
    MMperfGeoMean = MMperfGeoMean ^ (1/4);
    QSperfGeoMean = QSperfGeoMean ^ (1/4);
    % VC++ runs MM ops in 1.0221 of the time as GCC
    % VC++ runs QS ops in 0.8806 of the time as GCC
    % VC++ generally runs in 0.9487 of the time as GCC
    
    %   calculate geometric mean of performance ratios between computers
    %   W541 and T420s
    compMMPerfGeoMean = VSMMDebugRatio*VSMMReleaseRatio*GCCMMDebugRatio*GCCMMReleaseRatio;
    compQSPerfGeoMean = VSQSDebugRatio*VSQSReleaseRatio*GCCQSDebugRatio*GCCQSReleaseRatio;
    compPerfGeoMean = (compMMPerfGeoMean * compQSPerfGeoMean) ^ (1/8);
    
    compMMPerfGeoMean = compMMPerfGeoMean ^ (1/4);
    compQSPerfGeoMean = compQSPerfGeoMean ^ (1/4);
    % W541 runs MM ops in 0.8053 of the time as T420
    % W541 runs QS ops in 0.8655 of the time as T420
    % W541 generally runs in 0.8349 of the time as T420
end