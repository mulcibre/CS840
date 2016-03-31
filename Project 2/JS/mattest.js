var system = require('system');

var mat = new Array(10);

for(var i = 0; i < 10; i++)
{
    mat[i] = new Array(10);
}

var counter = 0;

for(var i = 0; i < 10; i++)
{
    for(var j = 0; j < 10; j++)
    {
        mat[i][j] = counter++;
    }
}

system.stdout.write(mat.length.toString() + "\n");

for(var i = 0; i < 10; i++)
{
    for(var j = 0; j < 10; j++)
    {
        system.stdout.write(mat[i][j].toString());
    }
}