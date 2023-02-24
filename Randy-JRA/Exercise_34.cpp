//Challenge 34 is to Create a function that will return an array with words inside a text
#include <iostream>
#include <stdio.h>
 
int main()
{
    // Initialize array of pointer
    const char* colour[4]
        = { "Blue", "Green", "Orange", "Red" };
 
    // Printing Strings stored in 2D array
    for (int i = 0; i < 4; i++)
        std::cout << colour[i] << "\n";
 
    return 0;
}
