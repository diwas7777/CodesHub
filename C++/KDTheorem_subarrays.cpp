// Finding the maximum sum of sub array using Kadanes theorem
// Actual KD Theorem(from internet) code:
// #include<bits/stdc++.h>
// using namespace std;

// int maxSumSubarray(vector<int> A) {
//     int maxsumSoFar = A[0];
//     int maxsumEndingHere = A[0];
//     for (int i = 1; i < A.size(); i = i + 1)
//     {
//         maxsumEndingHere = max (maxsumEndingHere + A[i], A[i]);
//         if (maxsumSoFar < maxsumEndingHere){
//             maxsumSoFar = maxsumEndingHere;
//     }

// }
//     return maxsumSoFar;

// }

#include <iostream>
using namespace std;

int sub_sum(int arr[], int n)
{
    int cs = 0, largest = 0;
    for (int i = 0; i < n; i++)
    {

        cs += arr[i];
        if (cs < 0)
        {
            cs = 0;
        }
        largest = max(cs, largest);
    }
    return largest;
}
int main()
{
    int arr[] = {1, -2, 3, 4, 4, -2};
    int n = sizeof(arr) / sizeof(int);
    cout << sub_sum(arr, n);

    return 0;
}
