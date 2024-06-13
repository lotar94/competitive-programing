// https://codeforces.com/problemset/problem/520/A
#include <bits/stdc++.h>
#include <iostream>
#include <algorithm>
#include <string>
#include <cctype>

using namespace std;

int main()
{
    string letters = "abcdefghijklmnopqrstuvwxyz";
    int n;
    string word;
    string resp = "YES";
    string result;

    cin >> n;
    cin >> word;

    std::transform(word.begin(), word.end(), word.begin(),
                   [](unsigned char c)
                   { return std::tolower(c); });

    std::vector<std::string> vec;

    for (size_t i = 0; i < word.length(); i += 1)
    {
        std::string substring = word.substr(i, 1);
        vec.push_back(substring);
    }
    if (word.length() >= 26)
    {
        for (char i : letters)
        {
            result = "";
            result += i;
            if (find(vec.begin(), vec.end(), result) != vec.end())
            {
            }
            else
            {
                resp = "NO";
                break;
            }
            result = "";
        }
    }
    else
    {
        resp = "NO";
    }

    cout << resp;
};