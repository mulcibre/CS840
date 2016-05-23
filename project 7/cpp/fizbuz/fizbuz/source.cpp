#include <iostream>

using namespace std;

int main()
{
	for (int i = 1; i <= 100; i++)
	{
		if (!(i % 3) && !(i % 5))
		{
			cout << "fizzbuzz\n";
		}
		else if (!(i % 3))
		{
			cout << "fizz\n";
		}
		else if (!(i % 5))
		{
			cout << "buzz\n";
		}
		else
		{
			cout << i << "\n";
		}
	}

	return 0;
}