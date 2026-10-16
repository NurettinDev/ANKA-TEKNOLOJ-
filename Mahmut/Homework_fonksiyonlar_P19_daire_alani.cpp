#include <iostream>
#include <string>
#include<cmath>

using namespace std;

float CircleArea(float Diameter, float pi)
{

	return pi * pow((Diameter / 2), 2);

}
int main()

{
	float Diameter;
	const float pi = 3.14;

	cout << ("Please enter the diameter") << endl;
	cin >> Diameter;
	cout << endl;

	cout << ("Area = ") << CircleArea(Diameter, pi) << endl;
}