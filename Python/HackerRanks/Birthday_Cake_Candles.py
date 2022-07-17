from collections import Counter

candles = [3,2,1,3,2,2,2]

print(Counter(candles).most_common(1)[0][1])

