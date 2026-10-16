#include <iostream>
#include <string>

using namespace std;

int RectangleArea(int Length, int Width)
{
	return Length * Width;
}

int main()
{
	int Length, Width;

	cout << ("Please enter the length") << endl;
	cin >> Length;
	cout << endl;

	cout << ("Please enter the width") << endl;
	cin >> Width;
	cout << endl;

	cout << ("Area = ") << RectangleArea(Length, Width) << endl << endl;
}