s = int(input())
responses = []
for x in range(s): 
    s = input()
    a = int(s.split(" ")[0]) 
    b = int(s.split(" ")[1]) 
    c = int(s.split(" ")[2])
    x = int(s.split(" ")[3])
    y = int(s.split(" ")[4])
    amount_food = a + b + c
    ammount_pets = x + y
    if x == a and y == b:
        responses.append("YES")
    elif amount_food >= ammount_pets and c != 0:
        responses.append("YES")
    else: 
        responses.append("NO")

for x in list(responses):
    print(x)
    
       

