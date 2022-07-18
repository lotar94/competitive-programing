grades = [73,67,38,33]


res = []
for x in grades:
  if x < 38:
      res.append(x)
  else:
    
    
    if (5-(x%5)) < 3:    
        res.append(x+(5-(x%5)))
    else:
        res.append(x)

for x in res:
    print(x)
