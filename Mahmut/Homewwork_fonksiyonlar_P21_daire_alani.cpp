#include <iostream>
#include <string>
#include<cmath>

using namespace std;

float CircleArea(float Circumference, float pi)
{

	return pow(Circumference, 2) / (4 * pi);

}
int main()

{
	float Circumference;
	const float pi = 3.14;

	cout << ("Please enter the circumference") << endl;
	cin >> Circumference;
	cout << endl;

	cout << ("Area = ") << CircleArea(Circumference, pi) << endl;
}