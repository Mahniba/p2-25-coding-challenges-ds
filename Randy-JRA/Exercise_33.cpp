//Challenge 33 is to Calculate the sum of numbers received in a comma delimited string
#include <iostream>
#include <sstream>

using namespace std;

int main() {
    string input = "1,2,3,4,5";
    int sum = 0;
    stringstream ss(input);
    string token;

    while (getline(ss, token, ',')) {
        sum += stoi(token);
    }

    cout << "Sum: " << sum << endl;

    return 0;
}

