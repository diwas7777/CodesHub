#include <bits/stdc++.h>
using namespace std;

void helper(int n , int o , int c, string s){
	
	if(c==n){
		cout<<s<<endl;
	}

	if(c<o ){
		helper(n,o,c+1,s+")");
	}
	
	if(o<n ){
		helper(n,o+1,c,s+"(");
	}

	
}

int main(){
	int n;
	cin>>n;

	helper(n,0,0,"");
	return 0;
}
