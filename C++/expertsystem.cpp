#include <iostream>
#include <stdio.h>
using namespace std;
void measels(char,char,char,char,char);
void flu(char,char,char,char,char,char,char,char);
int main()
{
char name[50];
char a,b,c,d,e,f,g,h,i,j,k;
cout << "Please enter your name.. " << endl;
cin>> name;
cout << "Do you have fever? (y/n)"<< endl;
cin>>a;
cout << "Do you have rashes? (y/n)"<< endl;
cin>>b;
cout << "Do you have headache? (y/n)"<< endl;
cin>>c;
cout << "Do you have running nose? (y/n)"<<
endl; cin>>d;
cout << "Do you have conjunctivities? (y/n)"<<
endl; cin>>e;
cout << "Do you have cough? (y/n)"<< endl;
cin>>f;
cout << "Do you have ache? (y/n)"<< endl;
cin>>g;
cout << "Do you have chills? (y/n)"<< endl;
cin>>h;
cout << "Do you have swollen glands? (y/n)"<<
endl; cin>>i;
cout << "Do you have snezzing? (y/n)"<< endl;
cin>>j;
cout << "Do you have sore throat? (y/n)"<< endl;
cin>>k;
measels(a,f,e,d,b);
flu(a,c,g,e,h,k,f,d);
return 0;
} ;
void measels(char q,char w,char r,char t,char y)
{
if(q=='y'&&w=='y'&& r=='y' && t=='y' && y==
'y') cout<< "You may have FLU."<< endl;
else
cout<< "";
}
void flu(char q,char w,char r,char t,char y,char p,char l,char x)
{
if(q=='y'&&w=='y'&& r=='y' && t=='y' && y== 'y'&& p=='y' && l=='y' &&
x=='y') cout<< "You may have COVID."<< endl;
else
cout<< "";
}
