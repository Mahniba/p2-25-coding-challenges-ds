//Challenge 50 is to Create a function that will receive n as argument and return an array of n
//random numbers from 1 to n

#include <iostream>
#include <cstdlib>
#include <ctime>

int* generateRandomArray(int n) {
    int* arr = new int[n]; // allocate memory for the array
    srand(time(NULL)); // seed the random number generator with current time
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % n + 1; // generate a random number between 1 and n
    }
    return arr; // return the array
}

int main() {
    int n = 10; // example usage
    int* arr = generateRandomArray(n);
    for (int i = 0; i < n; i++) {
        std::cout << arr[i] << " ";
    }
    delete[] arr; // free the memory allocated for the array
    return 0;
}
 

