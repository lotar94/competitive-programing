#include <iostream>
#include <algorithm>
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
            string aux = names[i];
            char letraT = 'T';
            char letrai = 'i';
            char letram = 'm';
            char letrau = 'u';
            char letrar = 'r';
            bool contieneT = find(aux.begin(), aux.end(), letraT) != aux.end();
            bool contienei = find(aux.begin(), aux.end(), letrai) != aux.end();
            bool contienem = find(aux.begin(), aux.end(), letram) != aux.end();
            bool contieneu = find(aux.begin(), aux.end(), letrau) != aux.end();
            bool contiener = find(aux.begin(), aux.end(), letrar) != aux.end();
            if (contieneT == true && contienei == true && contienem == true && contieneu == true && contiener == true)
            {
                response[i] = "YES";
            }
            else
            {
                response[i] = "NO";
            }
        }
        else
        {
            response[i] = "NO";
        }
    }

    for (size_t i = 0; i < testCases; i++)
    {
        cout << string(response[i]) << "\n";
    }
}
