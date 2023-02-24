//Challenge 29 is to Print the distance between the first 100 prime numbers

#include <iostream>
#include <cmath>
using namespace std;

bool is_prime(int n) {
    if (n <= 1) {
        return false;
    }
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int count = 0;
    int prev_prime = 0;
    for (int i = 2; count < 100; i++) {
        if (is_prime(i)) {
            if (prev_prime != 0) {
                cout << i - prev_prime << endl;
            }
            prev_prime = i;
            count++;
        }
    }
    return 0;
}
 
