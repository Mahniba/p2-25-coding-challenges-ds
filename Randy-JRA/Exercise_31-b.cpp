//Challenge 31-b is to Create a function that will return the number of words in a text
#include <iostream>
#include <string>
using namespace std;

int countWords(string text) {
    int count = 0;
    bool inWord = false;
    for (char c : text) {
        if (c == ' ' || c == '\n' || c == '\t') {
            inWord = false;
        } else if (!inWord) {
            inWord = true;
            count++;
        }
    }
    return count;
}

int main() {
    string text = "hello am called randy.";
    int numWords = countWords(text);
    cout << "Number of words: " << numWords << endl;
    return 0;
}
