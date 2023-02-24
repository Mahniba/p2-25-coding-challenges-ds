//Challenge 45 is to Create a function to calculate the sum of all the numbers in a jagged array (array contains numbers or other 
//arrays of numbers on an unlimited number of levels)


#include <iostream>
using namespace std;
// Function to calculate sum
void EvenOddSum(int arr[], int n)
{
	int even = 0;
	int odd = 0;
	for (int i = 0; i < n; i++) {
		// Loop to find even, odd sum
		if (i % 2 == 0)
			even += arr[i];
		else
			odd += arr[i];
	}

	cout << "Here Even index positions sum " << even;
	cout << "\nand Odd index positions sum " << odd;
}

int main()
{
	int arr[] = { 1, 2, 3, 4, 5, 6 };
	int n = sizeof(arr) / sizeof(arr[0]);

	EvenOddSum(arr, n);

	return 0;
}

