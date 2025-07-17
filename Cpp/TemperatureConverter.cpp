#include<iostream>
using namespace std;
class tempConvert
{
private:
    float C,F,K;
public:
    void CelsiusToFahrenheit()
    {
        cout<<"Enter value of temperature in Degree Celsius: \n";
        cin>>C;
        F=((9/5)*C)+32;
        cout<<C<<" Degree Celsius = "<<F<<" Degree Fahrenheit\n\n";
    }
    void FahrenheitToCelsius()
    {
        cout<<"Enter value of temperature in Degree Fahrenheit: \n";
        cin>>F;
        C=(F-32)*5/9;
        cout<<F<<" Degree Fahrenheit = "<<C<<" Degree Celsius\n\n";
    }
    void CelsiusToKelvin()
    {
        cout<<"Enter value of temperature in Degree Celsius: \n";
        cin>>C;
        K=C+273.15;
        cout<<C<<" Degree Celsius = "<<K<<" Kelvin\n\n";
    }
    void KelvinToCelsius()
    {
        cout<<"Enter value of temperature in Kelvin: \n";
        cin>>K;
        C=K-273.15;
        cout<<K<<" Kelvin = "<<C<<" Degree Celsius\n\n";
    }
    void FahrenheitToKelvin()
    {
        cout<<"Enter value of temperature in Degree Fahrenheit: \n";
        cin>>F;
        K=((5/9)*(F-32))+273.15;
        cout<<F<<" Degree Fahrenheit = "<<K<<" Kelvin\n\n";
    }void KelvinToFahrenheit()
    {
        cout<<"Enter value of temperature in Kelvin: \n";
        cin>>K;
        K=((9/5)*(K-273.15))+32;
        cout<<K<<" Kelvin = "<<F<<" Degree Fahrenheit\n\n";
    }

    void execute()
    {
        int d;
        cout<<"Welcome to The Temperature Converter!\n";
        do
            {
                cout<<"Choose Which Conversion would you like to make.\n";
                cout<<"1 Celsius to Fahrenheit\n2 Fahrenheit to Celsius\n3 Celsius to Kelvin\n4 Kelvin to Celsius\n5 Fahrenheit to Kelvin\n6 Kelvin to Fahrenheit\n7 Exit\n";
                cin>>d;
                switch(d)
                {
                case 1:
                    CelsiusToFahrenheit();
                    break;
                case 2:
                    FahrenheitToCelsius();
                    break;
                case 3:
                    CelsiusToKelvin();
                    break;
                case 4:
                    KelvinToCelsius();
                    break;
                case 5:
                    FahrenheitToKelvin();
                    break;
                case 6:
                    KelvinToFahrenheit();
                    break;
                case 7:
                    break;
                default:
                    cout<<"Invalid input!!\n\n";
                }
            }while (d!=7);
    }

};
int main()
{
    tempConvert t;
    t.execute();
    return 0;
}