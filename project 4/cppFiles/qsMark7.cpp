#include <iostream>
#include <chrono>
#include <random>

using namespace std;

/*
This quicksort algorithm is taken from
http://www.algolist.net/Algorithms/Sorting/Quicksort
*/
void quickSort(int arr[], int left, int right) {
	int i = left, j = right;
	int tmp;
	int pivot = arr[(left + right) / 2];

	/* partition */
	while (i <= j) {
		while (arr[i] < pivot)
			i++;
		while (arr[j] > pivot)
			j--;
		if (i <= j) {
			tmp = arr[i];
			arr[i] = arr[j];
			arr[j] = tmp;
			i++;
			j--;
		}
	};

	/* recursion */
	if (left < j)
		quickSort(arr, left, j);
	if (i < right)
		quickSort(arr, i, right);
}

int main()
{
	//	chrono::steady_clock has previously been established to have an error of 2.689e-07 seconds
	//	for these experiments, we must assume a total error of 5.378e-07 seconds
	//	due to the worst case scenario for two time measurements (start/stop)

	//	initialize timers
	chrono::steady_clock::time_point startTime, stopTime;
	double sortTime;

	//	initialize random generator, set generator type/range here
	random_device rd;
	mt19937 gen(rd());
	std::uniform_int_distribution<> dis(1, 1000000);

	//	array initialization
	int sortCount = 10;

	int arrSize = 1000000;
	int* toSort = new int[arrSize];

	for (int i = 0; i < arrSize; i++)
	{
		toSort[i] = dis(gen);
	}

	startTime = chrono::steady_clock::now();

	//	Call to sort function
	quickSort(toSort,0,arrSize-1);

	stopTime = chrono::steady_clock::now();
	sortTime = chrono::duration_cast<chrono::duration<double>>(stopTime - startTime).count() / sortCount;

	cout << sortTime << endl;

	return 0;
}