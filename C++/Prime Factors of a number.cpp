#include <iostream>
using namespace std;
int main() 
{
	int number, c, count = 0;

	cout << "\n\n Print all Prime factors of a number:\n";
	cout << "-----------------------------------\n";
	cout << " Input a number: ";
	while (!(cin >> number) || number < 0)
	{
		cout << "ERROR! Number is invalid.\nEnter a number again.";
		cin.clear();
		cin.ignore(123, '\n');
	}
	cout << "Prime Factors of " << number << " are as below.\n";
	for (c = 1; c <= number; c++)
	{
		if (number % c == 0)
		{
			count = 0;
			for (int i = 1; i <= (c / 2); i++)
			{
				if (c % i == 0)
					count++;
			}
			if (count == 1)
				cout << c << " ";
		}
	}
	return 0;
}

