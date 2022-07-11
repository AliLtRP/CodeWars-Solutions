def sum_of_minimums(numbers):
    result = 0
    for i in range(len(numbers)):
        for j in numbers[i]:
            d = min(numbers[i])
        result+=d
    return result
