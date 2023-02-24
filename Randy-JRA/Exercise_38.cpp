//Challenge 38 is to Create a function that will convert an array containing ASCII codes in a string

#include <iostream>
using namespace std;
 
int main()
{
int ascii;
cout<<"Enter ASCII: \n";
cin>>ascii;
char ch = char(ascii);
cout<<"Corresponding character is: "<<ch<<endl;
return 0;
}
 
