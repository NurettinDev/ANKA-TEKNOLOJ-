#include <iostream>
#include <string>

using namespace std;

struct strİnfo
{

	string Name;
	string Surname;
	string Fullname = Name + Surname;
	int Age;
	string City;
	string Country;
	int MonthlySalary;
	string Gender;
	bool Married;

};

void Readİnfo(strİnfo& info)
{

	cout << "Pleas enter the name:" << endl;
	cin >> info.Name;
	cout << endl;

	cout << "Pleas enter the surname:" << endl;
	cin >> info.Surname;
	cout << endl;

	info.Fullname = info.Name + " " + info.Surname;

	cout << "Pleas enter the age:" << endl;
	cin >> info.Age;
	cout << endl;

	cout << "Pleas enter the city:" << endl;
	cin >> info.City;
	cout << endl;

	cout << "Pleas enter the country:" << endl;
	cin >> info.Country;
	cout << endl;

	cout << "Pleas enter the montsalary:" << endl;
	cin >> info.MonthlySalary;
	cout << endl;

	cout << "Pleas enter the gender:" << endl;
	cin >> info.Gender;
	cout << endl;

	cout << "Are you married? (1: Yes, 0: No): " << endl;
	cin >> info.Married;
	cout << endl;

}

void Printİnfo(strİnfo info)
{

	cout << "******************************" << endl;
	cout << "Full Name: " << info.Fullname << endl;
	cout << "Age: " << info.Age << endl;
	cout << "City: " << info.City << endl;
	cout << "Country: " << info.Country << endl;
	cout << "Monthly salary: " << info.MonthlySalary << endl;
	cout << "Gende: " << info.Gender << endl;
	cout << "Married: " << info.Married << endl;
    cout << "******************************" << endl;

}

int main()
{

	strİnfo info_1;
	Readİnfo(info_1);
	Printİnfo(info_1);

}