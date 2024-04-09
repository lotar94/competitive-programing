case_test = input()

for i in range(int(case_test)):#2
    n = input()
    character = "#"    
    res = ""
    flagX = 1
    for i in range(int(n)*2):
        if flagX <= 2:
            res+=character
        else:
            print("1 => ", res[-1])
            print("1 => ", res[-2])
            if res[-1] == "#" and res[-2] == "#":
                character = "."
            elif res[-1] == "." and res[-2] == ".":
                character = "#"
            elif res[-1] == "." and res[-2] == "#":
                character = "."
            elif res[-1] == "#" and res[-2] == ".":
                character = "#"
            res+=character
            flagX = 0
        flagX = flagX+1

    print(res)