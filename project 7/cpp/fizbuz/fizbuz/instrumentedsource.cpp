
#include <iostream>
#include <fstream>
long long programBodyCounters[6] = { 0 };

using namespace std;

int main()
{
programBodyCounters[0]++;

	for (int i = 1; i <= 100; i++)
	{
programBodyCounters[1]++;

		if (!(i % 3) && !(i % 5))
		{
programBodyCounters[2]++;

			cout << "fizzbuzz\n";
		}
		else if (!(i % 3))
		{
programBodyCounters[3]++;

			cout << "fizz\n";
		}
		else if (!(i % 5))
		{
programBodyCounters[4]++;

			cout << "buzz\n";
		}
		else
		{
programBodyCounters[5]++;
			cout << i << "\n";
		}
	}

ofstream outfile;
outfile.open("../../../outfiles/fizbuzoutput.txt");
int codeExecCounterArraySize = sizeof(programBodyCounters) / sizeof(long long);
for (int i = 0; i < codeExecCounterArraySize - 1; i++)
{
outfile << programBodyCounters[i] << ",";
}
outfile << programBodyCounters[codeExecCounterArraySize - 1];
outfile.close();

	return 0;
}