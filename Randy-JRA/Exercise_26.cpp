//Challenge 26 is to Create a function that will receive two arrays and will return an array
//with elements that are in the first array but not in the second

#include<bits/stdc++.h>
using namespace std;
void findMissing(int a[], int b[],
                 int n, int m)
{
    for (int i = 0; i < n; i++)
    {
        int j;
        for (j = 0; j < m; j++)
            if (a[i] == b[j])
                break;
    		if (j == m)
            cout << a[i] << " ";
    }
}
 
int main()
{
    int a[] = { 1, 2, 6, 3, 4, 5 };
    int b[] = { 2, 4, 3, 1, 0 };
    int n = sizeof(a) / sizeof(a[0]);
    int m = sizeof(b) / sizeof(b[1]);
    findMissing(a, b, n, m);
    return 0;
}
