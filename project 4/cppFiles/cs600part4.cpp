//	hmw2part4.cpp : Sam Gluss 10/5/2015
//	you know it!
//	CS600 HMW2 Part 4: printing big integers

#include <iostream>
#include <string>
using namespace std;

int getDigitCount(int number)
{
	//counts the viable digits in the number
	int digitCount = 0;
	while (number) {
		number /= 10;
		digitCount++;
	}
	return digitCount;
}

char nthdigit(int number, int digitPos)
{
	//function which returns the character of the desired digit
	int retVal;
	while (digitPos--)
	{
		number /= 10;
	}
	retVal = (number % 10) + '0';
	return retVal;
}

void bigInt(int toPrint)
{
	string digit0[7] = {	" $$$$$ ",
							" $   $ ", 
							" $   $ ", 
							" $   $ ", 
							" $   $ ",
							" $   $ ",
							" $$$$$ ", };
	string digit1[7] = {	"   $   ",
							"  $$   ",
							" $$$   ",
							"   $   ",
							"   $   ",
							"   $   ",
							" $$$$$ ", };
	string digit2[7] = {	"  $$$  ",
							" $   $ ",
							"     $ ",
							"    $  ",
							"   $   ",
							"  $    ",
							" $$$$$ ", };
	string digit3[7] = {	"  $$$  ",
							" $   $ ",
							"     $ ",
							"   $$  ",
							"     $ ",
							" $   $ ",
							"  $$$  ", };
	string digit4[7] = {	"    $$ ",
							"  $$ $ ",
							" $   $ ",
							" $$$$$ ",
							"     $ ",
							"     $ ",
							"     $ ", };
	string digit5[7] = {	" $$$$$ ",
							" $     ",
							" $     ",
							"  $$$  ",
							"     $ ",
							" $   $ ",
							"  $$$  ", };
	string digit6[7] = {	"    $$ ",
							"   $   ",
							"  $    ",
							"  $$$  ",
							" $   $ ",
							" $   $ ",
							"  $$$  ", };
	string digit7[7] = {	" $$$$$ ",
							"     $ ",
							"     $ ",
							"    $  ",
							"    $  ",
							"   $   ",
							"   $   ", };
	string digit8[7] = {	"  $$$  ",
							" $   $ ",
							" $   $ ",
							"  $$$  ",
							" $   $ ",
							" $   $ ",
							"  $$$  ", };
	string digit9[7] = {	"  $$$  ",
							" $   $ ",
							" $   $ ",
							"  $$$  ",
							"     $ ",
							"     $ ",
							"   $$  ", };
		
	int digitCount = getDigitCount(toPrint);

	for (int line = 0; line < 7; line++)
	{
		//print each line, from top to bottom
		for (int i = 0; i < digitCount; i++)
		{
			//determine which digit to get a line from
			switch (nthdigit(toPrint, (digitCount - (i + 1))))
			{
				case '0':
					cout << digit0[line];
					break;
				case '1':
					cout << digit1[line];
					break;
				case '2':
					cout << digit2[line];
					break;
				case '3':
					cout << digit3[line];
					break;
				case '4':
					cout << digit4[line];
					break;
				case '5':
					cout << digit5[line];
					break;
				case '6':
					cout << digit6[line];
					break;
				case '7':
					cout << digit7[line];
					break;
				case '8':
					cout << digit8[line];
					break;
				case '9':
					cout << digit9[line];
					break;
			}
		}
		cout << endl;
	}
	cout << endl;
}

int main()
{
	//test some big Integer prints
	bigInt(2746);

	bigInt(1234567890);

	bigInt(5318008);
	system("pause");
	return 0;
}

