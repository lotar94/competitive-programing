#include <bits/stdc++.h>
#include <iostream>
using namespace std;
// test cambios
int main()
{
    // lista de los valores utilizar
    int array[8] = {-1, 2, 4, -3, 5, 2, -5, 2};
    int best = 0; // se guardara la mejor suma
    int n = 8;    // numero de elementos a recorrer

    // Recorremos la lista completa
    for (int a = 0; a < n; a++)
    {
        // recorremos
        for (int b = a; b < n; b++)
        {
            int sum = 0;
            for (int k = a; k <= b; k++)
            {
                // cout << array[k];
                sum += array[k];
            }
            best = max(best, sum);
        }
    }
    cout << best << "\n";
};
