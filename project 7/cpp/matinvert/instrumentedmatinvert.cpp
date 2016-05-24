
#include <iostream>
#include <fstream>
long long programBodyCounters[23] = { 0 };
#include <random>
#include <chrono>

using namespace std;

int main()
{
programBodyCounters[0]++;

	//	chrono::steady_clock has previously been established to have an error of 2.689e-07 seconds
	//	for these experiments, we must assume a total error of 5.378e-07 seconds
	//	due to the worst case scenario for two time measurements (start/stop)

	//	initialize random generator, set generator type/range here
	random_device rd;
	mt19937 gen(rd());
	std::uniform_int_distribution<> dis(1, 1000);

	//	initialize timers
	chrono::steady_clock::time_point startTime, stopTime;
	double initTime1;
	double invTime;
	double initTime2;
	double multTime2;

	double initTimes[25];
	double invTimes[25];
	int iteration = 0;

	for (int rowCount = 20; rowCount <= 500; rowCount += 20) {
programBodyCounters[1]++;


		//	matrix A/B initialization
		int initRepCount = 200 / sqrt(rowCount);
		int multRepCount = 200 / sqrt(rowCount);
		int** matA = new int*[rowCount];

		startTime = chrono::steady_clock::now();
		for (int K = 0; K < initRepCount; K++)
		{
programBodyCounters[2]++;

			for (int i = 0; i < rowCount; i++)
			{
programBodyCounters[3]++;

				matA[i] = new int[rowCount];

				//	initialize rows to random values
				for (int j = 0; j < rowCount; j++)
				{
programBodyCounters[4]++;

					matA[i][j] = dis(gen);
				}
			}
		}
		stopTime = chrono::steady_clock::now();
		initTime1 = chrono::duration_cast<chrono::duration<double>>(stopTime - startTime).count() / initRepCount;
	
		startTime = chrono::steady_clock::now();
		for (int K = 0; K < multRepCount; K++)
		{
programBodyCounters[5]++;

			
			/*
			begin inversion code from numerical recipes 2nd ed
			*/
			int* indxc = new int[rowCount];
			int* indxr = new int[rowCount];
			int* ipiv = new int[rowCount];
			int i, icol = 0, irow = 0, j, k, l, ll;
			double big, dum, pivinv, temp;
			int* temp2;
			for (j = 0; j<rowCount; ++j)
				ipiv[j] = 0;
			for (i = 0; i<rowCount; ++i)
			{
programBodyCounters[6]++;

				big = 0.0;
				for (j = 0; j<rowCount; ++j)
				{
programBodyCounters[7]++;

					if (ipiv[j] != 1)
					{
programBodyCounters[8]++;

						for (k = 0; k<rowCount; ++k)
						{
programBodyCounters[9]++;

							if (ipiv[k] == 0)
							{
programBodyCounters[10]++;

								if (fabs(matA[j][k]) >= big)
								{
programBodyCounters[11]++;

									big = fabs(matA[j][k]);
									irow = j;
									icol = k;
								}
							}
							else
							{
programBodyCounters[12]++;

								if (ipiv[k] > 1)
								{
programBodyCounters[13]++;

									//	Something bad happened?
								}
							}
						}
					}
				}
				++ipiv[icol];
				if (irow != icol)
				{
programBodyCounters[14]++;

					temp2 = matA[irow];
					matA[irow] = matA[icol];
					matA[icol] = temp2;
				}
				indxr[i] = irow;
				indxc[i] = icol;
				if (matA[icol][icol] == 0.0)
				{
programBodyCounters[15]++;

					//	Something bad happened?
				}
				pivinv = 1.0 / matA[icol][icol];
				matA[icol][icol] = 1.0;
				for (l = 0; l<rowCount; ++l)
					matA[icol][l] *= pivinv;
				for (ll = 0; ll<rowCount; ++ll)
				{
programBodyCounters[16]++;

					if (ll != icol)
					{
programBodyCounters[17]++;

						dum = matA[ll][icol];
						matA[ll][icol] = 0.0;
						for (l = 0; l<rowCount; ++l)
							matA[ll][l] -= matA[icol][l] * dum;
					}
				}
			}
			for (l = rowCount - 1; l >= 0; --l)
			{
programBodyCounters[18]++;

				if (indxr[l] != indxc[l])
				{
programBodyCounters[19]++;

					for (k = 0; k<rowCount; ++k)
					{
programBodyCounters[20]++;

						temp = matA[k][indxr[l]];
						matA[k][indxr[l]] = matA[k][indxc[l]];
						matA[k][indxc[l]] = temp;
					}
				}
			}
			/*
			end inversion code
			*/

		}
		stopTime = chrono::steady_clock::now();
		invTime = chrono::duration_cast<chrono::duration<double>>(stopTime - startTime).count() / multRepCount;
		
		initTimes[iteration] = initTime1;
		invTimes[iteration] = invTime;
		iteration++;
		//end of execution for each rowcount test
	}

	cout << "init times:\n";
	for (int i = 0; i < 25; i++)
	{
programBodyCounters[21]++;

		cout << initTimes[i] << ",";
	}
	cout << "\n\ninversion times:\n";
	for (int i = 0; i < 25; i++)
	{
programBodyCounters[22]++;
		cout << invTimes[i] << ",";
	}
ofstream outfile;
outfile.open("../../outfiles/matinvertoutput.txt");
int codeExecCounterArraySize = sizeof(programBodyCounters) / sizeof(long long);
for (int i = 0; i < codeExecCounterArraySize - 1; i++)
{
outfile << programBodyCounters[i] << ",";
}
outfile << programBodyCounters[codeExecCounterArraySize - 1];
outfile.close();

	return 0;
}