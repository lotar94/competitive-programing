#include <iostream>
using namespace std;

int main()
{

    int testCases;
    cin >> testCases;
    string names[testCases];
    string response[testCases];

    string name;
    string lengthName;

    for (int i = 0; i < testCases; i++)
    {
        cin >> lengthName;
        cin >> name;
        names[i] = name;
    }

    for (int i = 0; i < testCases; i++)
    {
        if (names[i].length() == 5)
        {
        }
        else
        {
            response[i] = "NO";
        }
    }
}