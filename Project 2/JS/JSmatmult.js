var system = require('system');

var startTime;
var endTime;
var multTime;
var multTimes = [];

for (var rowCount = 20; rowCount <= 500; rowCount += 20) {
    
    var a = new Array(rowCount);
    var b = new Array(rowCount);
    var c = new Array(rowCount);

    var multRepCount = 3 + Math.floor(Math.pow(100, 3) / Math.pow(rowCount, 3));
    startTime = performance.now();
    for (var K = 0; K < multRepCount; K++)
    {
        for(var i=0; i<rowCount; i++) 
        {
            a[i] = new Array(rowCount);
            b[i] = new Array(rowCount);
            c[i] = new Array(rowCount);
            
            //	initialize rows to desired values
            for(var j=0; j<rowCount; j++) {
                if(i == j)
                {
                    a[i][j] = 2.002;
                    b[i][j] = 2.002;
                }
                else
                {
                    a[i][j] = 1.001;
                    b[i][j] = 1.001;
                }
                c[i][j] = 0;
            }
        } 
            //	Populate C with appropriate values
        for(var k = 0; k<rowCount; k++) {
            for(var j = 0; j<rowCount; j++) {
                for(var i = 0; i<rowCount; i++) {
                    c[j][i] += a[k][i]*b[j][k];
                }
            }
        }
        
    }
    endTime = performance.now();
    //  get duration, convert to seconds from ms
    multTime = (endTime - startTime) / (multRepCount * 1000);
    multTimes.push(multTime);
}

for (i = 0; i < multTimes.length; i++)
{
    system.stdout.write(multTimes[i].toString());
    if(i < multTimes.length - 1)
    {
        system.stdout.write(',');
    }
}
system.stdout.write("\n");

phantom.exit(0);