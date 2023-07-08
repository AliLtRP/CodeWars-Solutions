def sum_array(arr):
    
    if  arr == None or len(arr) <= 1:
        return 0
    else:
        arr.sort()
        del arr[0], arr[-1]
        return sum(arr)
