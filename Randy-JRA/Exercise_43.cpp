//Challenge 43 is to Create a function that will receive a bidimensional array as argument and a number and will extract as a
//unidimensional array the column specified by the number

#include<iostream>
using namespace std;

void processArr(int a[][2]) {
   cout << "element at col 1,1 is " << a[1][1];
}
int main() {
   int arr[2][2];
   arr[0][0] = 0;
   arr[0][1] = 1;
   arr[1][0] = 2;
   arr[1][1] = 3;

   processArr(arr);
   return 0;
}
