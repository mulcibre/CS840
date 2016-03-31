// hmw2part3.cpp : Defines the entry point for the console application.
// Samuel Gluss
// CS600 Homework 2 Part 3
// Array Reduce
// 10/5/2015

#include <iostream>
#include <stdlib.h>

using namespace std;

void printElements(int *&array, int length)
{
	//useful function we can use to print the elements in a dynamic array
	cout << "array elements:" << endl;
	for (int i = 0; i < length; i++)
	{
		cout << array[i] << " ";
	}
	cout << endl;
}

void reduce(int *&array, int& length)
{
	int top1 = 0, top2 = 0, top3 = 0, sizeCounter = 0, reducedArrayIndex = 0;

	//get the values of the highest valued items in the array
	for (int i = 0; i < length; i++)
	{
		if (array[i] > top3)
		{
			if (array[i] > top2)
			{
				if (array[i] > top1)
				{
					top3 = top2;
					top2 = top1;
					top1 = array[i];
				}
				else if (array[i] != top1)
				{
					top3 = top2;
					top2 = array[i];
				}
			}
			else if (array[i] != top2)
			{
				top3 = array[i];
			}
		}
	}

	//print top 3 values
	cout << "highest values: " << top1 << " " << top2 << " " << top3 << endl;

	//determine size of reduced array
	for (int i = 0; i < length; i++)
	{
		if (array[i] < top3)
		{
			sizeCounter++;
		}
	}

	//allocate new array to hold the reduced array values
	int *reducedArray = new int[sizeCounter];

	//initialize reduced array
	for (int i = 0; i < length; i++)
	{
		if (array[i] < top3)
		{
			reducedArray[reducedArrayIndex] = array[i];
			reducedArrayIndex++;
		}
	}

	//reassign the original matrix
	delete(array);
	array = reducedArray;
	length = sizeCounter;
}

int main()
{

	//create our initial array
	int arraySize = 20;
	int *myArray = new int[arraySize];

	//populate the array with some random values from 1 to 100
	for (int i = 0; i < arraySize; i++)
	{
		myArray[i] = rand() % 100 + 1;
	}

	//print our initial array
	printElements(myArray, arraySize);

	reduce(myArray, arraySize);

	//print the reduced array
	printElements(myArray, arraySize);

	system("PAUSE");

	return 0;
}
