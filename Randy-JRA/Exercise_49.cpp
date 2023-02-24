//Challenge 49 is to Shuffle an array of strings

#include <bits/stdc++.h>
using namespace std;

// Shuffle array
void shuffle_array(char arr[], int n)
{

	// To obtain a time-based seed
	unsigned seed = 0;

	// Shuffling our array
	shuffle(arr, arr + n,
			default_random_engine(seed));

	// Printing our array
	for (int i = 0; i < n; ++i)
		cout << arr[i] << " ";
	cout << endl;
}

// Driver code
int main()
{
	const char* a[5] = {"apple", "randy", "orange", "kiwi", "jam"};

	int n = sizeof(a) / sizeof(a[0]);

	shuffle_array(a, n);

	return 0;
}

 
