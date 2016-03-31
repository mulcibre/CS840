var system = require('system');
console.log('Hello, world');

var numTimes = 10;
var times = [];

for(var i = 0; i < numTimes; i++)
{
    times[i] = performance.now();
}

var durations = [];
for(var i = 0; i < numTimes - 1; i++)
{
    durations[i] = times[i+1] - times[i];
}

for(var i = 0; i < numTimes - 1; i++)
{
    system.stdout.write(durations[i].toString());
    if(i < numTimes - 2)
    {
        system.stdout.write(',')
    }
    else
    {
        system.stdout.write("\n")
    }
}

phantom.exit(0);