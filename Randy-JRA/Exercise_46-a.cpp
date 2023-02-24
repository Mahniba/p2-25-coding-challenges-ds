//Challenge 46-a is to Find the maximum number in a jagged array of numbers or array of number using recursion


#include <bits/stdc++.h>
using namespace std;

int largest(int arr[], int n)
{
	int i;
	
	// Initialize maximum element
	int max = arr[0];

	// Traverse array elements
	// from second and compare
	// every element with current max
	for (i = 1; i < n; i++)
		if (arr[i] > max)
			max = arr[i];

	return max;
}

int main()
{
	int arr[] = {10,42,455,1234,3};
	int n = sizeof(arr) / sizeof(arr[0]);
	cout << "Largest in given array is "
		<< largest(arr, n);
	return 0;
}
