def dont_give_me_five(start,end):
    not_welcoming = '5'
    str_lists = []
    result = 0
    for i in range(start , end+1):
        str_lists.append(str(i))
    for j in str_lists:
        if not_welcoming not in j:
            result+=1
    return result
