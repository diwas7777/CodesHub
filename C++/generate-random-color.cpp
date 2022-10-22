#include<iostream>
#include<stdlib.h>
#include<time.h>
using namespace std;
 
void rgb_color_code(int rgb[]);

void rgb_color_code(int rgb[])
{
  int i;
  for(i=0;i<3;i++)
  {
    rgb[i]=rand()%256;
  }
}

int main()
{
  int rgb[3];
  char hex[6];
    srand(time(0));
    
    //RGB color code
    rgb_color_code(rgb);
  cout<<"Random RGB color code: ";
  cout<<"rgb(";
  for(int i=0;i<3;i++)
  {
    cout<<rgb[i];
    //to seperate red, blue, color values by a comma( no comma for last value)
    if(i!=2)
    {
      cout<<", ";
    }
  }
  cout<<")"<<endl;
  
  return 0;
}
