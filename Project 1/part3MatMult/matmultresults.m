initTimes = [0.000314809,0.00125467,0.00279878,0.00497755,0.0077674,0.0111735,0.0151968,0.0198023,0.0250046,0.0309519,0.0374806,0.0444943,0.0521777,0.0605702,0.0694805,0.0790187,0.089222,0.099837,0.11132,0.1235,0.136048,0.149398,0.163331,0.177621,0.193023];
multTimes = [2.21094e-05,0.000185637,0.000608034,0.0014362,0.00286703,0.00478017,0.00756775,0.0116817,0.016601,0.0228369,0.0315675,0.0414805,0.0550665,0.0703848,0.0912619,0.114135,0.139784,0.1654,0.20318,0.236833,0.281416,0.317488,0.372892,0.415152,0.483338];

initCoeff = polyfit(20:20:500,initTimes,2);
multCoeff = polyfit(20:20:500,multTimes,3);

% for ax^3 + bx^2 :
b = initCoeff(1);
b2 = multCoeff(2);
a = multCoeff(1);

figure
scatter(20:20:500,initTimes);
hold on;
scatter(20:20:500, multTimes, '+');
 title('Matrix initialization vs Multiplication');
    ylabel('Time (s)')
    xlabel('Matrix Size (NxN)');
    legend('Initialization','Multiplication')

figure
subplot(1,2,1);
scatter(20:20:500,initTimes + multTimes);
hold on;
scatter(20:20:500, a*(20:20:500).^3 + (b + b2)*(20:20:500).^2, '+');
 title('Matrix Multiplication');
    ylabel('Time (s)')
    xlabel(['Matrix Size (NxN) A=' num2str(a) ' B=' num2str(b)]);
    legend('Measured','Predicted')
   
    subplot(1,2,2);
    errors = bsxfun(@rdivide,(abs((a*(20:20:500).^3 + (b + b2)*(20:20:500).^2)) - (initTimes + multTimes)),(initTimes + multTimes));
    scatter(20:20:500, errors);
    hold on;
    p1 = [0,0];
    p2 = [0,500];
    plot([p1(2),p2(2)],[p1(1),p2(1)],'Color','b','LineWidth',1);
    title('Matrix Multiplication Model Error');
    ylabel('Error Proportion')
    xlabel('Matrix Size (NxN)');
    