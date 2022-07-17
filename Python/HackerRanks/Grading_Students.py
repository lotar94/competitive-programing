grades = [73, 67, 38, 33]


res = []
for x in grades:
  if x < 38:
      res.append(x)
  else:
    print(x%5)
    if (x%5) <= 3:    
        res.append(x)
    else:
        res.append(x)
