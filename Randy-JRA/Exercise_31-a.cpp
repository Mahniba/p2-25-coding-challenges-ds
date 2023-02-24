//Challenge 31-a is to Create a function that will return the number of words in a text
#include <iostream>
#include <string>

using namespace std;

int countWords(string text) {
    int count = 0;
    bool inWord = false;

    for (int i = 0; i < text.length(); i++) {
        if (isalpha(text[i])) {
            if (!inWord) {
                count++;
                inWord = true;
            }
        }
        else {
            inWord = false;
        }
    }

    return count;
}

int main() {
    string text = "Name is Jam Randy";
    int wordCount = countWords(text);
    cout << "Number of words: " << wordCount << endl;
    return 0;
}
 
