#include <iostream>
#include <string>
#include <cmath>

using namespace std;

float RectangleArea(float Length, float Diagonal)
{

		return Length * sqrt(pow (Diagonal, 2) - pow (Length, 2));

}

int main()
{
	float Length, Diagonal;

	cout << ("Please enter the length") << endl;
	cin >> Length;
	cout << endl;

	cout << ("Please enter the diagonal") << endl;
	cin >> Diagonal;
	cout << endl;

	cout << ("Area= ") << RectangleArea(Length, Diagonal);
}