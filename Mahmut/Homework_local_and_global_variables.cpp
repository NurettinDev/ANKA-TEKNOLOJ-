#include <iostream>
#include <string>

using namespace std;

string name = "Mahmut";
int age = 22;

void MyFunction()
{

	string name = "HAYDAR";

	cout << ("Name: ") << name << endl;

}

int main()
{

	int age = 23;

	cout << ("Age: ") << age << endl;
	MyFunction();

	cout << ("Global Name and age: ") << ::name << (" ") << ::age << endl;

}