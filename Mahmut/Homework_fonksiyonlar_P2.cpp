#include <iostream>
#include <string>

using namespace std;

void MyName()
{

	string FullName;
	cout << ("Please enter your full name") << endl;
	getline(cin, FullName);
	cout << endl;
	cout << ("My name is ") + FullName << endl << endl;

}

int main()
{
	MyName();
}