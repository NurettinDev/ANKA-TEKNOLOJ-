#include <iostream>
#include <string>

using namespace std;

int TotalSeconds(int Days, int Hours, int Minutes, int Seconds)
{

	int TotalSeconds = Days * 86400 + Hours * 3600 + Minutes * 60 + Seconds;

	return TotalSeconds;

}

int main()
{
	int Days, Hours, Minutes, Seconds;

	cout << ("Please enter the days") << endl;
	cin >> Days;
	cout << endl;

	cout << ("Please enter the hours") << endl;
	cin >> Hours;
	cout << endl;

	cout << ("Please enter the minutes") << endl;
	cin >> Minutes;
	cout << endl;

	cout << ("Please enter the seconds") << endl;
	cin >> Seconds;
	cout << endl;

	cout << ("Total Seconds = ") << TotalSeconds(Days, Hours, Minutes, Seconds) << endl <<endl;
}