#include <iostream>
#include <string>

using namespace std;

void ReadGrades(float Grades[3])
{

	cout << "Please enter grade 1?" << endl;
	cin >> Grades[0];
	cout << endl;

	cout << "Please enter grade 2?" << endl;
	cin >> Grades[1];
	cout << endl;

	cout << "Please enter grade 3?" << endl;
	cin >> Grades[2];
	cout << endl;

}

float Avages(float Grades[3])
{

	return (Grades[0] + Grades[1] + Grades[2]) / 3;

}

void PrintGrades(float Grades[3])
{
	cout << "Avages = " << Avages(Grades) << endl;
}

int main()
{

	float Grades[3];
	ReadGrades(Grades);
	PrintGrades(Grades);

}