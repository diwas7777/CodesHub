#include<iostream>
using namespace std;
int DecToBin(int n){
    if(n==0){
        return 0;
    }else{
        return (n%2+10*(DecToBin(n/2)));
    }
}
int main(){
    cout<<DecToBin(7)<<"\n";
    return 0;
}