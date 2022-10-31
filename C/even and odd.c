#include<stdio.h>
int main()
{
  int i,n,even=0,odd=0;
  printf("\nEnter the Ending value:");
  scanf("%d",&n);
  printf("\nEven numbers:");
  for(i=0;i<=n;i++)
  {
    if(i%2==0)
    {
      printf("\n%d",i);
      even++;
    }
  }
  printf("\nOdd numbers:");
  for(i=1;i<=n;i++)
  {
    if(i%2==1)
    {
      printf("\n%d",i);
      odd++;
    }
  }
  printf("\nTotal even numbers:%d",even);
  printf("\nTotal odd numbers:%d",odd);
    return 0;
    }
