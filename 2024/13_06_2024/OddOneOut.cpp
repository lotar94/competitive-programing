// https://codeforces.com/problemset/problem/1915/A
#include <iostream>

using namespace std;

int main()
{
    int t;
    string a, b, c;

    cin >> t;
    string array[int(t)][3];
    string resp[t];

    for (int i = 0; i < int(t); i++)
    {
        cin >> a;
        cin >> b;
        cin >> c;
        array[i][0] = a;
        array[i][1] = b;
        array[i][2] = c;
    }

    for (int i = 0; i < t; i++)
    {
        if (array[i][0] == array[i][1])
            resp[i] = (array[i][2]);
        if (array[i][1] == array[i][2])
            resp[i] = (array[i][0]);
        if (array[i][0] == array[i][2])
            resp[i] = (array[i][1]);
    }

    for (size_t i = 0; i < t; i++)
    {
        cout << string(resp[i]) << "\n";
    }
}
