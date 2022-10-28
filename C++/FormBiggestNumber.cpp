# include <bits/stdc++.h>
using namespace std;

bool possible(string a , string b){
	    
	    string ab = a.append(b);
	    string ba = b.append(a);
	    int res = 0 ;
	    for(int i = 0 ; i < ab.size() ; i++){
	        if(ab[i]>ba[i]){
	            res = 1;
	            break;
	        }else if(ab[i] < ba[i]){
	            res = -1;
	            break;
	        }
	    }
	    
	    if(res>0){
	        return false;
	    }else{
	        return true;
	    }
	    
	}

int main(){
	int t;
	cin>>t;

	while(t--){

		int n;
		cin>>n;
	
		string arr[n];
		for(int i = 0 ; i<n ;i++ ){
			cin>>arr[i];
		}

		for(int i = 0 ; i < n-1 ; i++){
			for(int j = 0 ; j < n-1 ; j++){

				
				if(possible(arr[j],arr[j+1])){
					string temp = arr[j];
					arr[j] = arr[j+1];
					arr[j+1] = temp;
				}
			}
		}

		for(int i = 0 ; i<n ;i++ ){
			cout<<arr[i];
		}cout<<endl;

	}
	return 0;
}
