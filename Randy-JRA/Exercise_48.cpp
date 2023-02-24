//Challenge 48 is to Create a function to return the longest word(s) in a string

#include <iostream>
using namespace std;

string longestWordInSentence(string str) {
    // we write the algorithm to count the number of words in the above string literal/ sentence
    int words = 0;
    for (int i = 0; i < str.length(); i++) {
        if (str[i] == ' ') {
            words++;
        }
    }
    words += 1;  
    string strWords[words];

    // this algorithm appends the individual words in the array strWords
    short counter = 0;
    for (short i = 0; i < str.length(); i++) {
        strWords[counter] += str[i];
        if (str[i] == ' ') {
            counter++;
        }
    }

    // algorithm to find the longest word in the strWords array
    int sizeArray = sizeof(strWords) / sizeof(strWords[0]);  
    int longest = strWords[0].length();  
    string longestWord = "";             
    for (int i = 0; i < sizeArray; i++) {  
        if (strWords[i].length() > longest) {
            longest = strWords[i].length();
            longestWord = strWords[i];  
        }
    }

    return longestWord;  // return the longest word in the sentence
}

int main() {
    string x = "I love solving garri and chips with flippedmeatpie";
    cout << longestWordInSentence(x);
    return 0;
}
