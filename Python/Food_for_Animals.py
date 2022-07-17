s = int(input())
responses = []
for x in range(s): 
    s = input()
    a = int(s.split(" ")[0]) 
    b = int(s.split(" ")[1]) 
    c = int(s.split(" ")[2])
    x = int(s.split(" ")[3])
    y = int(s.split(" ")[4])
    if x+y <= c:
        responses.append("YES")
    elif x <= a and y <= b:
        responses.append("YES")
    elif x <= a+(c-b) and y <= b+(c-a):
        responses.append("YES")
    elif x <= a+c and y <= b:
        responses.append("YES")
    elif x <= a and y <= b+c:
        responses.append("YES")
    elif x <= c and y <= b:
        responses.append("YES")
    elif x <= a and y <= c:
        responses.append("YES")
    else: 
        responses.append("NO")


for x in list(responses):
    print(x)
    

