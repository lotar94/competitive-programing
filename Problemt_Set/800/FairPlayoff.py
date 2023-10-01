# Link problem https://codeforces.com/problemset/problem/1535/A
def is_fair_tournament(skills):
    skills.sort(reverse=True)  # Ordena las habilidades en orden descendente
    if (skills[0] > skills[1] and skills[2] > skills[3]) or (skills[0] < skills[1] and skills[2] < skills[3]):
        return "YES"
    else:
        return "NO"

# Lectura de entrada
t = int(input())  # Número de casos de prueba
for _ in range(t):
    skills = list(map(int, input().split()))  # Habilidades de los jugadores en el caso de prueba
    result = is_fair_tournament(skills)
    print(result)
