#include <iostream>
#include <string>
#include<cmath>

using namespace std;

float CircleArea(float Side, float pi)
{

	return pi * pow((Side / 2), 2);

}
int main()

{
	float Side;
	const float pi = 3.14;

	cout << ("Please enter the side") << endl;
	cin >> Side;
	cout << endl;

	cout << ("Area = ") << CircleArea(Side, pi) << endl;
}