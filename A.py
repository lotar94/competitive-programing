
numTestCase = input()
digits = []

for i in range(int(numTestCase)):
    digits.append(list(input().split()))

for i in digits:
    a = i[0]
    b = i[1]
    c = i[2]
    if a < b and b < c:
        print("STAIR")
    elif a < b and b > c:
        print("PEAK")
    else:
        print("NONE")


