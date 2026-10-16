#include <iostream>
#include <string>
#include<cmath>

using namespace std;

void power(int Number)
{

	int Square = pow(Number, 2);
	int Cube = pow(Number, 3);
	int Power4 = pow(Number, 4);


	cout << ("Square = ") << Square << endl;
	cout << ("Cube = ") << Cube << endl;
	cout << ("Power4 = ") << Power4 << endl << endl;

}


int main()
{
	int Number;
	cout << ("Please enter the number") << endl;
	cin >> Number;
	cout << endl << endl;

	power(Number);
}