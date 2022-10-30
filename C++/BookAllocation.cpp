#include <bits/stdc++.h>
using namespace std;

bool possible(int books[] , int nbooks, int stds , int checkmax){

	

	int currsum = 0 ;
	int allocatedto = 1;
	for(int i = 0 ; i < nbooks ; i++){

		if (books[i] > checkmax) {
            return false;
        }

		if(currsum + books[i] <= checkmax){
			currsum+=books[i];
		}else{
			allocatedto++;
			currsum = books[i];
		}
		if(allocatedto>stds){
			return false;
		}
	}
	return true;
}

int allocate(int books[] , int nbooks ,int stds){

	int res = INT_MAX;
	int st = 0 ;

	int sum=0;
	for(int i = 0 ; i < nbooks ; i++){
		sum+=books[i];
	}
	int en = sum;

	while(st<=en){
		int mid = (st+en)/2;
		if(possible(books,nbooks,stds,mid)){
			res = min(mid,res);
			en = mid-1;
		}else{
			st = mid+1;
		}
	}

	return res;


}

int main() {

	int t;
	cin>>t;
	while(t--){

		int nbooks,stds;
		cin>>nbooks>>stds;
		
		int books[nbooks];
		for(int i = 0 ; i < nbooks; i++){
			cin>>books[i];
		}
		
		cout<<allocate(books,nbooks,stds)<<endl;


	}


	return 0;
}

