# Link problem https://codeforces.com/problemset/problem/1535/A
def is_fair_tournament(skills):
    match1 = [skills[0], skills[1]]
    skills.sort(reverse=True)  # Ordena las habilidades en orden descendente
    if ((skills[0] in match1) == True and (skills[1] in match1) == True): # Si los 2 mas altos estan en el primer match no es juesto
        return "NO"
    elif ((skills[0] in match1) == False and (skills[1] in match1) == False): # Si los 2 mas altos NO estan en el primer match no es juesto
        return "NO"
    else:
        return "YES"

# Lectura de entrada
t = int(input())  # Número de casos de prueba
for _ in range(t):
    skills = list(map(int, input().split()))  # Habilidades de los jugadores en el caso de prueba
    result = is_fair_tournament(skills)
    print(result)
