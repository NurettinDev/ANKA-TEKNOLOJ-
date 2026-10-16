#include <iostream>
#include <string>
#include<cmath>

using namespace std;

float CircleArea(float Side_a, float Side_b, float Side_c, float pi)
{
	float p = (Side_a + Side_b + Side_c) / 2;
	return pi * pow((Side_a * Side_b * Side_c) / (4 * sqrt(p * (p - Side_a) * (p - Side_b) * (p - Side_c))), 2);

}
int main()

{
	float Side_a, Side_b, Side_c;
	const float pi = 3.14;

	cout << ("Please enter the side a") << endl;
	cin >> Side_a;
	cout << endl;

	cout << ("Please enter the side b") << endl;
	cin >> Side_b;
	cout << endl;

	cout << ("Please enter the side c") << endl;
	cin >> Side_c;
	cout << endl;

	cout << ("Area = ") << CircleArea(Side_a, Side_b, Side_c, pi) << endl;
}