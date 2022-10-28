//PROGRAM TO CALCULATE AMOUNT OF RAIN WATER TRAPPED
#include<iostream>

using namespace std;

class TrapWater{

    
    public:
    //Function to find the amount of trapped water between the blocks
    int trappingWater(int arr[], int n)
    {
        int ToatalWaterTrap=0 , Larr[n] , Rarr[n] ;

        Larr[0]=arr[0];
        for(int i = 1 ; i < n ; i++)
        {
            Larr[i] = (arr[i]>Larr[i-1])? arr[i]:Larr[i-1] ;
        }

        Rarr[n-1]=arr[n-1];
        for(int i = n-2 ; i >= 0 ; i--)
        {
            Rarr[i] = (arr[i]>Rarr[i+1])? arr[i]:Rarr[i+1] ;
        }

        for(int i = 0 ; i < n ; i++)
        {
            ToatalWaterTrap += (Larr[i]>Rarr[i])? (Rarr[i]-arr[i]):(Larr[i]-arr[i]) ;
        }

        return ToatalWaterTrap;
        
    }
};

int main()
{
    int size;

    cout<<"\nEnter size of array : "; //getting size of array from user
    cin>>size;

    while(size<1) // size should be >=1
    {
       cout<<"\n[ERROR] Invalid size ##try again##";
       cout<<"\nEnter size of array : ";
       cin>>size;   
    }

    int arr[size];

    cout<<"\nEnter height of all the "<<size<<" blocks : "; // getting block size from user
    for(int i=0;i<size;i++)
    {
        cin>>arr[i];

    }

    for(int i=0;i<size;i++)
    {
        while(arr[i]<0)
        {
            cout<<"\n[ERROR] Invalid height of "<<i+1<<" block ##try again";
            cout<<"\nEnter height of the "<<i+1<<" block : ";
            cin>>arr[i];
        }
    }

    TrapWater tw ;

    cout<<"\nTotal Units Of Water Trapped In Blocks : "<<tw.trappingWater(arr,size);
    cout<<endl;

    return 0;
}
