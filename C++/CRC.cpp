#include <iostream>
#include <string>
using namespace std;

string XOR1(string p, string q)
{
    string XORval = "";
    for (int i = 0; i < q.length(); i++)
    {
        if (p[i] == q[i])
            XORval += "0";
        else
            XORval += "1";
    }
    // cout << "xor: " << XORval << endl;
    return XORval;
}

string divXOR(string dividend, string divisor)
{
    int divLen = divisor.length();
    // taking out the number of bits to be XORed at a time.
    string sub_dividend = dividend.substr(0, divLen);
    // cout << sub_dividend << endl;
    int dividendLen = dividend.length();
    while (divLen < dividendLen + 1)
    {
        if (sub_dividend[0] == '1')
        {
            sub_dividend = XOR1(divisor, sub_dividend).substr(1, sub_dividend.length() - 1) + dividend[divLen];
        }
        else
        {
            sub_dividend = sub_dividend.substr(1, sub_dividend.length() - 1) + dividend[divLen];
        }
        divLen++;
        // cout << "sd" << sub_dividend << endl;
    }
    return sub_dividend;
}

void encryptData(string dataBlock, string divisor)
{
    int divlen = divisor.length();
    string appended_dataBlock = dataBlock;
    // for (int i = 0; i < divlen-1; i++)
    // {
    //     appended_dataBlock += '0';
    // }
    appended_dataBlock = (dataBlock + string(divlen - 1, '0'));
    // cout << "appended_data" << appended_dataBlock << endl;
    string remainder = divXOR(appended_dataBlock, divisor);
    string encrypted_data = dataBlock + remainder;
    cout << "Original DataBlock: " << dataBlock << endl;
    cout << "Remainder: " << remainder << endl;
    cout << "Encrypted DataBlock: " << encrypted_data << endl;
}
void checkError(string dataBlock, string divisor)
{
    int divlen = divisor.length();
    string remainder = divXOR(dataBlock, divisor);
    string appended_bits = string(divlen - 1, '0');
    // cout
    //     << "\n\n\n\nremainder:" << remainder << endl
    //     << "appended bits:" << appended_bits << endl;
    // if (remainder == appended_bits)
    // {
    //     cout << "Valid DataBlock!\n";
    // }
    // else
    //     cout << "Error: Invalid DataBlock!\n";
    for (int i = 0; i < divlen - 1; i++)
    {
        if (remainder[i] != appended_bits[i])
        {
            cout << "Error: Invalid DataBlock!\n";
            return;
        }
    }
    cout << "Valid DataBlock!\n";
}

int main()
{
    cout << "Enter 1 for Sender, 2 for Reciever: ";
    int n;
    cin >> n;
    string dataBlock;
    string divisor;
    switch (n)
    {
    case 1:
        cout << "Enter the dataBlock: ";
        // getline(cin, dataBlock);
        cin >> dataBlock;
        cout << "Enter the divisor: ";
        // getline(cin, divisor);
        cin>>divisor;
        encryptData(dataBlock, divisor);
        break;
    case 2:
        cout << "Enter the dataBlock: ";
        // getline(cin, dataBlock);
        cin >> dataBlock;
        cout << "Enter the divisor: ";
        // getline(cin, divisor);
        cin >> divisor;
        checkError(dataBlock, divisor);
        break;

    default:
        cout << "Invalid Choice!";
        exit(0);
        break;
    }

    return 0;
}