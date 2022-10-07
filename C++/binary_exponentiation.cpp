#include <bits/stdc++.h>
#include<vector>

using namespace std;

#define ll long long
#define ld long double
#define pb push_back
#define F first
#define S second
#define rep(i,j,k) for(ll i=j;i<k;i++)
#define endl "\n"
#define N 10000010
long long binpow(long long a, long long b)
{
    long long res = 1;
    while (b > 0)
    {
        if (b & 1)
            res = res * a;
        a = a * a;
        b >>= 1;
    }
    return res;
}

void solve()
{cout<<"enter the number "<<endl;
ll a;
cin>>a;
cout<<"enter the power"<<endl;
ll b;
cin>>b;
cout<<binpow(a,b)<<" this is the result of pow(a,b) by binary exponentiation"<<endl;




    }
int main()
{
   //freopen("input.txt", "r", stdin);
   //freopen("ans.txt", "w", stdout);
   ios_base::sync_with_stdio(false); cin.tie(NULL);
   int t=1;
    //cin>>t;
   rep(i,0,t) solve();
   return 0;
}