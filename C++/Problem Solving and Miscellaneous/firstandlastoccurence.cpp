#include<bits/stdc++.h>
using namespace std;
int first_occurence(int arr[],int n,int key){
    int s=0,e=n-1;
    int mid=s+(e-s)/2;
    int ans=-1;
    while(s<=e){
        if(arr[mid]==key){
            ans=mid;
            e=mid-1;
        }
        else if(arr[mid]<key){
            s=mid+1;
        }
        else if(arr[mid]>key){
            e=mid-1;
        }
        mid=s+(e-s)/2;
    }
    return ans;   
    }

int last_occurence(int arr[],int n,int key){
    int s=0,e=n-1;
    int mid=s+(e-s)/2;
    int ans=-1;
    while(s<=e){
        if(arr[mid]==key){
            ans=mid;
            s=mid+1;
        }
        else if(arr[mid]<key){
            s=mid+1;
        }
        else if(arr[mid]>key){
            e=mid-1;
        }
        mid=s+(e-s)/2;
    }
    return ans;   
    }
int main(){
    
    int even[11]={1,2,3,4,5,5,5,5,5,6,7};
    cout<<"First Occurence of 5 is at index: "<<first_occurence(even,11,5)<<endl;
    cout<<"Last Occurence of 5 is at index: "<<last_occurence(even,11,5)<<endl;
    cout<<"Frequency of 5: "<<last_occurence(even,11,5)-first_occurence(even,11,5)+1;
    
    return 0;
}
