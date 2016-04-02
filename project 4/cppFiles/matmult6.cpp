#include <iostream>
#include <chrono>

using namespace std;

int main()
{
	//	chrono::steady_clock has previously been established to have an error of 2.689e-07 seconds
	//	for these experiments, we must assume a total error of 5.378e-07 seconds
	//	due to the worst case scenario for two time measurements (start/stop)

	//	initialize timers
	chrono::steady_clock::time_point startTime, stopTime;
	double multTime;

	double multTimes[25];
	int iteration = 0;

	int rowCount = 500;
	//	matrix A/B initialization
	double multRepCount = 10;

	double** a = new double*[rowCount];
	double** b = new double*[rowCount];
	double** c = new double*[rowCount];
	for (int i = 0; i < rowCount; i++)
	{
		a[i] = new double[rowCount];
		b[i] = new double[rowCount];
		c[i] = new double[rowCount];
	}

	startTime = chrono::steady_clock::now();
	for (int K = 0; K < multRepCount; K++)
	{
		for (int i = 0; i < rowCount; i++)
		{
			//	initialize rows to desired values
			for (int j = 0; j < rowCount; j++)
			{
				if (i == j)
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
		for (int k = 0; k < rowCount; k++) {
			for (int j = 0; j < rowCount; j++) {
				for (int i = 0; i < rowCount; i++) {
					c[j][i] += a[k][i] * b[j][k];
				}
			}
		}
	}
	stopTime = chrono::steady_clock::now();
	multTime = chrono::duration_cast<chrono::duration<double>>(stopTime - startTime).count() / multRepCount;

	//	clean memory
	for (int i = 0; i < rowCount; i++) {
		delete[] a[i];
		delete[] b[i];
		delete[] c[i];
	}
	delete[] a;
	delete[] b;
	delete[] c;

	multTimes[iteration] = multTime;
	iteration++;

	cout << multTime << endl;

	return 0;
}