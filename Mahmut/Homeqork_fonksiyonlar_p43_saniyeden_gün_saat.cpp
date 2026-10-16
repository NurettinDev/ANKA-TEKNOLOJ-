#include <iostream>
#include <string>

using namespace std;

void ConvertSeconds(int TotalSeconds)
{

	int Days = TotalSeconds / 86400;
	int Remainder = TotalSeconds % 86400;

	int Hours = Remainder / 3600;
	Remainder = Remainder % 3600;

	int Minutes = Remainder / 60;
	int RemainingSeconds = Remainder % 60;

	cout << Days << ":" << Hours << ":" << Minutes << ":" << RemainingSeconds;


}

int main()
{
	int TotalSeconds;

	cout << ("Please enter the seconds") << endl;
	cin >> TotalSeconds;
	cout << endl;

	cout << ("Convert Seconds = ");
	ConvertSeconds(TotalSeconds);
}
	
