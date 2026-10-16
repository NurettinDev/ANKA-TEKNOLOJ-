#include <iostream>
#include <string>

using namespace std;

void Swap(int &Num1, int &Num2)
{

	int Temp;

	Temp = Num1;
	Num1 = Num2;
	Num2 = Temp;

	cout << "After swap inside function Num1 = " << Num1 << ", Num2 = " << Num2 << endl;
}

int main()
{
	int Num1, Num2;

	cout << ("Please enter the num 1: ");
	cin >> Num1;
	cout << endl;

	cout << ("Please enter the num 2: ");
	cin >> Num2;
	cout << endl;

	cout << "Before swap num 1 = " << Num1 << ", num 2 = " << Num2 << endl;

	Swap(Num1, Num2);

	cout << "After swap inside main the function num 1 = " << Num1 << ", num 2 = " << Num2 << endl;
}