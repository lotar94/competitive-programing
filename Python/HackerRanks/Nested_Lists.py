if __name__ == '__main__':
    data = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        data.append({"n":name, "s":score})

    data_sorted = sorted(data, key=lambda x: x['s'])
    
    

    second_lowest_grade_in = []
    more_lowest_grade = data_sorted[0]
    for x in data_sorted:
        if x['s'] != more_lowest_grade['s']:
            second_lowest_grade_in.append(x)
            break

    aux = [ val for val in data_sorted if val['s'] == second_lowest_grade_in[0]['s']]

    result  = sorted(aux, key=lambda x:x['n'])

    for x in result:
      print(x['n'])

