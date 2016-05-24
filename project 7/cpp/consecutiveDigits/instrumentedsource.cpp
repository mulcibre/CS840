
// hmw2part1.cpp : Defines the entry point for the console application.
// Samuel Gluss
// CS 600 Homework 2 Part 1
// 10/4/2015

#include <iostream>
#include <fstream>
long long programBodyCounters[10] = { 0 };
#include <stdlib.h>
#include <algorithm>

using namespace std;

void printElements(int *&array, int length)
{
programBodyCounters[0]++;

	//useful function we can use to print the elements in a dynamic array
	cout << "array elements:" << endl;
	for (int i = 0; i < length; i++)
	{
programBodyCounters[1]++;

		cout << array[i] << " ";
	}
	cout << endl << endl;
}

int maxlen(int *&testArray, int& length)
{
programBodyCounters[2]++;


	//find the longest string of consecutive numbers in the sorted array
	int currentMax = testArray[0];
	int currentMaxCounter = 1;

	int runnerUp = 0;
	int runnerUpCounter = 0;

	for (int i = 1; i < length; i++)
	{
programBodyCounters[3]++;

		//if next value is the same as running current max, increment maxcounter
		if (currentMax == testArray[i])
		{
programBodyCounters[4]++;

			currentMaxCounter++;
		}
		//if next element is a runnerup element, increment runnerupCounter
		else if (runnerUp == testArray[i])
		{
programBodyCounters[5]++;

			runnerUpCounter++;

			//if runnerup has the same count or greater than current max, change runnerup to be new longest string
			if (runnerUpCounter >= currentMax)
			{
programBodyCounters[6]++;

				currentMaxCounter = runnerUpCounter;
				runnerUpCounter = 0;
				currentMax = runnerUp;
				runnerUp = 0;
			}
		}
		//if next element is neither a max or a runnerup, start runnerup over with new value and counter
		else
		{
programBodyCounters[7]++;

			runnerUp = testArray[i];
			runnerUpCounter = 1;
		}
	}
	return currentMaxCounter;
}

int main()
{
programBodyCounters[8]++;

	//create our initial array
	int arraySize = 100;
	int *testArray = new int[arraySize];

	//populate the array with some random values from 1 to 25
	for (int i = 0; i < arraySize; i++)
	{
programBodyCounters[9]++;
		testArray[i] = rand() % 25 + 1;
	}

	cout << "unsorted array:" << endl;
	printElements(testArray, 100);

	//sort the array using algorithm library sort
	sort(testArray, testArray + 100);

	cout << "sorted array:" << endl;
	printElements(testArray, 100);

	//execute the maxlen function here, output the results
	cout << "Longest consecutive digit string has length of " << maxlen(testArray, arraySize) << endl;

ofstream outfile;
outfile.open("../../outfiles/consecutiveDigitsoutput.txt");
int codeExecCounterArraySize = sizeof(programBodyCounters) / sizeof(long long);
for (int i = 0; i < codeExecCounterArraySize - 1; i++)
{
outfile << programBodyCounters[i] << ",";
}
outfile << programBodyCounters[codeExecCounterArraySize - 1];
outfile.close();

	return 0;
}