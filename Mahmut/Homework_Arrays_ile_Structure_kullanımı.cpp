#include <iostream>
#include <string>

using namespace std;

struct strİnfo
{

	string Name;
	string LastName;
	int Age;
	string Phone;

};

void Readİnfo(strİnfo& info)
{

	cout << "Please enter firstname" << endl;
	cin >> info.Name;
	cout << endl;

	cout << "Please enter lastname" << endl;
	cin >> info.LastName;
	cout << endl;

	cout << "Please enter age" << endl;
	cin >> info.Age;
	cout << endl;

	cout << "Please enter phone" << endl;
	cin >> info.Phone;
	cout << endl;

}

void Printİnfo(strİnfo info)
{

	cout << "*******************************" << endl;
	cout << "Name: " << info.Name << endl;
	cout << "LastName: " << info.LastName << endl;
	cout << "Age: " << info.Age << endl;
	cout << "Phone: " << info.Phone << endl;
	cout << "*******************************" << endl << endl << endl;

}

void ReadPersonsİnfo(strİnfo persons[2])
{

	Readİnfo(persons[0]);
	Readİnfo(persons[1]);

}

void PrintPersonsİnfo(strİnfo persons[2])
{

	Printİnfo(persons[0]);
	Printİnfo(persons[1]);

}
int main()
{

	strİnfo persons[2];
	ReadPersonsİnfo(persons);
	PrintPersonsİnfo(persons);
}