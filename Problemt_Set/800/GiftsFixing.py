#https://codeforces.com/problemset/problem/1399/B

def needed_movements(n_giffs, a, b ):
    minor = sorted(a)[0]
    higher = sorted(bf)[0]
    print("Minor => ", minor)
    print("Higher => ", minor)
    print(n_giffs)
    print(a)
    print(b)



# Lectura de entrada
t = int(input())  # Número de casos de prueba
for _ in range(t):
    n_giffs = int(input())
    a = list(map(int, input().split()))  # Dulces
    b = list(map(int, input().split()))  # Naranjas 

    result = needed_movements(n_giffs, a, b)
    print(result)