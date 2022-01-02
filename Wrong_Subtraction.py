values = input().split()
#5120 4
count = 0
res = 0

n = values[0]

while int(values[1]) != count:  
    if n[-1:] == '0':
        res = int(int(n)/10)
    else:
        res = int(n) - 1
    
    count += 1
    n = str(res)

print(res)