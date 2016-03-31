classdef pingSession
    properties
        title
        pingCount
        timeoutCount
        latencies
    end
    
    methods
       % methods, including the constructor are defined in this block
       function obj = pingSession(a, b, c, d)
           obj.title = a;
           obj.pingCount = b;
           obj.timeoutCount = c;
           obj.latencies = d;
       end
    end
end