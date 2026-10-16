#include <iostream>
#include <string>
#include<cmath>

using namespace std;

float CircleArea(float Side, float Base, float pi)
{

	return pi * (pow(Base, 2) / 4) * ((2 * Side - Base) / (2 * Side + Base));

}
int main()

{
	float Side, Base;
	const float pi = 3.14;

	cout << ("Please enter the side") << endl;
	cin >> Side;
	cout << endl;

	cout << ("Please enter the base") << endl;
	cin >> Base;
	cout << endl;

	cout << ("Area = ") << CircleArea(Side, Base, pi) << endl;
}