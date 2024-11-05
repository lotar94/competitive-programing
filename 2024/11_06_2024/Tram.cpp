// https://codeforces.com/problemset/problem/116/A
#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main()
{
    int testCase = 0;
    cin >> testCase;
    int res = 0;
    int arr[testCase];

    for (int i = 0; i < testCase; i++)
    {
        int a = 0;
        int b = 0;
        cin >> a >> b;
        if (i == 0)
        {
            res = a + b;
        }
        else
        {
            res = (res - a) + b;
        }
        arr[i] = res;
    }

    int max = arr[0];

    for (int i = 1; i < testCase; ++i)
    {
        if (arr[i] > max)
        {
            max = arr[i];
        }
    }
    cout << max;
};