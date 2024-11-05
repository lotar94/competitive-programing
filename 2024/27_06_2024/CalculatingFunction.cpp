#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main()
{

    long long n;
    int r;
    cin >> n;

    for (size_t i = 1; i <= n; i++)
    {
        if (i == 1)
        {
            r = -1;
        }
        else if ((i % 2) == 0)
        {

            r = r + i;
        }
        else
        {

            r = r + -i;
        }
    }

    cout << r;
}