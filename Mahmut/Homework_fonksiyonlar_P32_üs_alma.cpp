#include <iostream>
#include <string>
#include<cmath>

using namespace std;

int power(int Number, int Exponent)
{
	return pow(Number, Exponent);
}


int main()
{
	int Number, Exponent;
	cout << ("Enter the number") << endl;
	cin >> Number;

	cout << ("Enter the exponent") << endl << endl;
	cin >> Exponent;

	cout <<("Result = ") << power(Number, Exponent) << endl << endl;
}