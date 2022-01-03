s = input()

count_uppercase = 0
count_lowercase = 0

for x in list(s):
    if x.isupper():
        count_uppercase += 1
    else:
        count_lowercase += 1

if count_lowercase <= count_uppercase:
    print(s.lower())
else:
    print(s.upper())