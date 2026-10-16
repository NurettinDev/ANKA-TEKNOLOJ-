#include <iostream>
#include <string>

using namespace std;

void Swap()
{

	float Num1, Num2, Temp;

	cout << ("Please enter num1") << endl;
	cin >> Num1;
	cout << ( "Num1 = ") << Num1 << endl << endl;

	cout << ("Please enter num2") << endl;
	cin >> Num2;
	cout<< ("Num2 = ") << Num2 << endl << endl;

	Temp = Num1;
	Num1 = Num2;
	Num2 = Temp;

	cout << ("Swap:") << endl;
	cout << ("Num1 = ") << Num1 << endl << endl;
	cout << ("Num2 = ") << Num2 << endl << endl;

}

int main()
{
	Swap();
}