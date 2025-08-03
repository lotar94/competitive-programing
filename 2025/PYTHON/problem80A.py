n, m = input().split(" ")

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

res = "NO"
aux = int(n)+1
while aux <= int(m):
    if(is_prime(int(aux))):
        if aux == int(m):
            res = "YES"
        break
    aux+= 1


print(res)


