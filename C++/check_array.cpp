// C++ program to find given two array
// are equal or not
#include <bits/stdc++.h>
using namespace std;

// Returns true if arr1[0..n-1] and arr2[0..m-1]
// contain same elements.
bool areEqual(int arr1[], int arr2[], int N, int M)
{
	// If lengths of array are not equal means
	// array are not equal
	if (N != M)
		return false;

	// Sort both arrays
	sort(arr1, arr1 + N);
	sort(arr2, arr2 + M);

	// Linearly compare elements
	for (int i = 0; i < N; i++)
		if (arr1[i] != arr2[i])
			return false;

	// If all elements were same.
	return true;
}

// Driver's Code
int main()
{
	int arr1[] = { 3, 5, 2, 5, 2 };
	int arr2[] = { 2, 3, 5, 5, 2 };
	int N = sizeof(arr1) / sizeof(int);
	int M = sizeof(arr2) / sizeof(int);

	// Function call
	if (areEqual(arr1, arr2, N, M))
		cout << "Yes";
	else
		cout << "No";
	return 0;
}
