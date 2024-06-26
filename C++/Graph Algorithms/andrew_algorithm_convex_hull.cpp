#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
typedef pair<int, int> ii;

int cross(ii O, ii A, ii B)
{
    return (((A.X - O.X) * (B.Y - O.Y)) - ((A.Y - O.Y) * (B.X - O.X)));
}

vector<ii> ConvexHull(vector<ii> P)
{
	if(P.size() <= 1) return P;
    vector<ii> H(2*P.size());
    int k = 0;
    sort(P.begin(), P.end());
    //lower hull
    for(int i = 0; i < P.size(); i++)
    {
        while(k >= 2 and cross(H[k-2], H[k-1], P[i]) < 0) k--;
        H[k++] = P[i];
    }
    //upper hull
    for(int i = P.size()-2, l = k + 1; i >= 0; i--)
    {
        while(k >= l and cross(H[k-2], H[k-1], P[i]) < 0) k--;
        H[k++] = P[i];
    }
    H.resize(k-1);
    return H;
}

int main()
{
    int n, x, y;
    vector<ii> P;
    
    cin >> n;
    while(n--)
    {
        cin >> x >> y;
        P.push_back({x, y});
    }

    vector<ii> H = ConvexHull(P);   

    for(int i = 0; i < H.size(); i++)
        cout << H[i].X << ' ' << H[i].Y << '\n';

	return 0;
}
