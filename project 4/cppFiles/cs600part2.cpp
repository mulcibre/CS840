#include <iostream>

void print(int a, int b, int c, int x1, int x3)
{
}

int determinant(int a, int b, int c, int d, int e, int f, int g, int h, int i)
{
	int retVal = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g);
	return retVal;
}

void calculateCoefficientsCramers(int x1, int y1, int x2, int y2, int x3, int y3)
{
	//use cramers rule to calculate coefficients for quadratic function

	//calculate determinant of coefficient matrix (D) first
	int det = determinant(x1*x1, x1, 1, x2*x2, x2, 1, x3*x3, x3, 1);

	if (det == 0)
	{
		std::cout << "determinant of coefficient matrix is zero, Cramers rule is not applicable";
		return;
	}

	//calculate coefficients for y = ax^2 + bx + c

	// a = Da / D
	int a = determinant(y1, x1, 1, y2, x2, 1, y3, x3, 1) / det;

	// b = Db / D
	int b = determinant(x1*x1, y1, 1, x2*x2, y2, 1, x3*x3, y3, 1) / det;

	// c = Dc / D
	int c = determinant(x1*x1, x1, y1, x2*x2, x2, y2, x3*x3, x3, y3) / det;
}

void calculateCoefficientsLagrange(int x1, int y1, int x2, int y2, int x3, int y3)
{
	//calculate 
	double denom1 = (x1 - x2)*(x1 - x3);
	double denom2 = (x2 - x1)*(x2 - x3);
	double denom3 = (x3 - x1)*(x3 - x2);

	double a = (y1 / denom1) + (y2 / denom2) + (y3 / denom3);

	double b = -(((y1 * (x2 + x3)) / denom1) + ((y2 * (x1 + x3)) / denom2) + ((y3 * (x1 + x2)) / denom3));

	double c = ((y1 * x2 * x3) / denom1) + ((y2 * x1 * x3) / denom2) + ((y3 * x1 * x2) / denom3);
}

int main()
{
	//test points
	int x1 = 1;
	int y1 = 9;
	int x2 = 2;
	int y2 = 23;
	int x3 = 3;
	int y3 = 45;

	if (x1 != x2 && x2 != x3 && x1 != x3)
	{
		calculateCoefficientsCramers(x1, y1, x2, y2, x3, y3);

		calculateCoefficientsLagrange(x1, y1, x2, y2, x3, y3);
	}
	else
	{
		std::cout << "All x values must be unique" << std::endl;
	}

	return 0;
}

