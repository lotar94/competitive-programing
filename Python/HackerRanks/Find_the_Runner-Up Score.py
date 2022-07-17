if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    newList = []
    for element in arr:
      if (element in newList) == False:
        newList.append(element)
      
    print(sorted(newList)[-2])
    
    