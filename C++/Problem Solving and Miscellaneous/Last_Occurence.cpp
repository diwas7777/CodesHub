#include<bits/stdc++.h>
using namespace std;
int last_occurance(int a[],int n,int k)
{
    int mid,l=0,h=n-1;     
   while(l<=h)
    {
        mid=(l+h)/2;
        if(a[mid]>k)
        h=mid-1;
        else if(a[mid]<k)
        l=mid+1;
        else 
        {
          if(a[mid+1]!=a[mid] || mid==n-1)
            return mid;
        else
           l=mid+1;
       }
    }
    return -1;
}
int main()
{
    int n;
    cin>> n;
    int k;
    cin>>k;
    int a[n];
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    int t=last_occurance(a,n,k);
    cout<<t<<" ";
}
