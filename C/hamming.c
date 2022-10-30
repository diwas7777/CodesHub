//Tushar
//HAMMING CODE WITH EVEN PARITY
#include<stdio.h>
#include<string.h>
#include<math.h>

int main()
{

    int data[20],hamming[50] , count=0;
    char cdata[20];
    printf("Enter data(bits) : ");
     scanf("%s",cdata);
    for(int i=0 ; i<strlen(cdata) ;i++)
    {
        data[i]=cdata[i]-'0';
    }
    int n=1;
    for(int i =0 ;i<=14;i++)
    {
        if(pow(2,n)>=strlen(cdata)+n)
        {
            break;
        }
        else
        {
            n++;
        }

    }
    int h=n+strlen(cdata);
    count=strlen(cdata)-1;

    for(int i=0 ; i<h ;i++)
    {
        if((ceil(log2(i+1))) != (floor(log2(i+1))))
        {
            hamming[i]=data[count--];
        }
        else
        {
            hamming[i]=0;//intiall storing all parity bits as zero
        }
    }

    count=0;
    //program to calculate parity bits
    for(int i=0 ; i<n ; i++)
    {
        int z=0 ;
        
        for(int j=pow(2,i)-1 ;j<h ;j++)
        {
            count+=hamming[j];
            z++;

            if(z==pow(2,i))
            {
                j+=pow(2,i);
                z=0;
            }
        }
        int x=pow(2,i)-1;
        if(count%2==0)
        {
            hamming[x]=0;
        }
        else
        {
            hamming[x]=1;
        } 
        count=0;  
    }

    //hamming code 
    printf("Hamming code :");
    for(int i=h-1 ; i>=0 ;i--)
    {
       printf("%d",hamming[i]);
    }

    return 0;
}
