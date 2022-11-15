def str_count(strng, letter):
    result = 0
    if strng =='':
        result = 0 
    else:
        for i in strng:
            for j in letter:
                if i==j:
                    result +=1
    return result 