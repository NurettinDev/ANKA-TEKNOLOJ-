#include <iostream>
#include <string>
#include<cmath>

using namespace std;

float CircleArea(float radius, float pi)
{

	return pi * pow(radius, 2);

}
int main()

{
	float radius;
	const float pi = 3.14;

	cout << ("Please enter the radius") << endl;
	cin >> radius;
	cout << endl;

	cout << ("Area = ") << CircleArea(radius, pi) << endl;
}