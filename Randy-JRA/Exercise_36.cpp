//Challenge 36 is to Create a function that converts a string to an array of characters
#include <iostream>
#include <string.h>

using namespace std;

int main()
{
    cout << "\n\nWelcome toTheNationalday :-)\n\n\n";
    cout << " =====  Program to convert a String to an array of characters  ===== \n\n";

    string s;

    cout << "\n\nEnter a String without any space : ";
    cin >> s;

    cout << "\n\nThe array containing the characters of the strings as it's element is: "
         << "\n\n";

    //The array of characters to be printed
    char cArray[1024];

    //This is an in-built method defined within the string.h library
    strncpy(cArray, s.c_str(), sizeof(cArray));

    //Initializing all the elements of the array to 0, all at once.
    cArray[sizeof(cArray) - 1] = 0;

    //declaring the loop variable within the loop is syntactically correct, but it's scope remains limited to the loop.
    for (int i = 0; cArray[i] != 0; i++)
    {
        cout << "\n cArray[ " << i << " ] :   " << cArray[i];
    }

    cout << "\n\n";

    return 0;
}
