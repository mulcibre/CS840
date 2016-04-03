// hmw2part5.cpp : Defines the entry point for the console application.
// Samuel Gluss
// CS 600 Homework 2 Part 5
// Performance of iterative and recursive binary search
// 10/5/2015

#include <iostream>
#include <chrono>
#include <stdlib.h>
#include <algorithm>
#include <random>

using namespace std;

int iterativeBinarySearch(int *&array, int size, int target)
{
	int foundIndex = 0;
	int low = 0;
	int high = size - 1;
	int mid = 0;

	//search loop
	while (low <= high)
	{
		mid = (low + high) / 2;
		if (array[mid] > target)
		{
			high = mid - 1;
		}
		else if (array[mid] < target)
		{
			low = mid + 1;
		}
		else
		{
			return mid;
		}
	}
}

int recursiveBinarySearch(int *&array, int target, int low, int high)
{
	if (high < low)
	{
		return -1;
	}
	//set mid to midpoint, use this to section the array for search
	int mid = (low + high) / 2;

	if (array[mid] > target)
	{
		return recursiveBinarySearch(array, target, low, mid - 1);
	}
	else if (array[mid] < target)
	{
		return recursiveBinarySearch(array, target, mid + 1, high);
	}
	else
	{
		return mid;
	}
}

int main()
{
	//create our initial array
	int arraySize = 100000000;
	int *testArray = new int[arraySize];

	cout << "populating array..." << endl;

	//populate the array with some random values from 1 to 25
	for (int i = 0; i < arraySize; i++)
	{
		testArray[i] = i;
	}

	//setting up the random number generator
	srand(time(NULL));
	std::default_random_engine generator;
	std::uniform_int_distribution<int> distribution(1, arraySize);

	//set up timer to measure duration of tests
	std::chrono::time_point<std::chrono::system_clock> start, end, start2, end2;

	int testsToRun = 1000000;
	int target = 0;
	int result = 0;

	cout << endl << "testing iterative search:" << endl;
	//testing the iterative search
	start = std::chrono::system_clock::now();
	for (int i = 0; i < testsToRun; i++)
	{
		target = distribution(generator);
		//disable cout statement for live tests
		//cout << "found : " << iterativeBinarySearch(testArray, arraySize, target) << endl;
		result = iterativeBinarySearch(testArray, arraySize, target);
	}
	end = std::chrono::system_clock::now();
	std::chrono::duration<double> elapsed_seconds = end - start;
	
	cout << endl << "testing recursive search:" << endl;
	//testing the recursive search
	start2 = std::chrono::system_clock::now();
	for (int i = 0; i < testsToRun; i++)
	{
		target = distribution(generator);
		//disable cout statement for live tests
		//cout << "found : " << recursiveBinarySearch(testArray, target, 0, arraySize - 1) << endl;
		result = recursiveBinarySearch(testArray, target, 0, arraySize - 1);
	}
	end2 = std::chrono::system_clock::now();
	std::chrono::duration<double> elapsed_seconds2 = end2 - start2;

	cout << "Duration of iterative searches: " << elapsed_seconds.count() << "s" << endl;
	cout << "Duration of recursive searches: " << elapsed_seconds2.count() << "s" << endl;

	system("pause");
	return 0;
}