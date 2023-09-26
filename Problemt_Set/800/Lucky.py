x = input()
for i in range(int(x)):
    y = list(input())
    sum1 = int(y[0]) + int(y[1]) +int(y[2])
    sum2 = int(y[3]) + int(y[4]) +int(y[5])
    
    if sum1 == sum2:
        print("YES")
    else:
        print("NO")

