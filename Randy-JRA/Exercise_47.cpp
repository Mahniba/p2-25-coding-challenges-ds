//Challenge 47 is to Deep copy a jagged array with numbers or other arrays in a new array

#include <iostream>
#include <vector>
using namespace std;

int main() {
    // define the original jagged array
    int arr1[3][4] = {
        {1, 2, 3},
        {4, 5},
        {6, 7, 8, 9}
    };

    // define the new jagged array
    vector<vector<int>> arr2;

    // loop through the original array and copy each subarray to the new array
    for (int i = 0; i < 3; i++) {
        vector<int> subarray;
        for (int j = 0; j < 4; j++) {
            if (j < sizeof(arr1[i])/sizeof(arr1[i][0])) {
                subarray.push_back(arr1[i][j]);
            }
        }
        arr2.push_back(subarray);
    }

    // print the original and new arrays
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
            cout << arr1[i][j] << " ";
        }
        cout << endl;
    }

    for (int i = 0; i < arr2.size(); i++) {
        for (int j = 0; j < arr2[i].size(); j++) {
            cout << arr2[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
 
