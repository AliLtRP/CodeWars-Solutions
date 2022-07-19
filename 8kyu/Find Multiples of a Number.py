def find_multiples(integer, limit):
    result = []
    
    for i in range(limit +1):
        y=i*integer
        if y <=limit and y !=0:
            result.append(y)
    return result
