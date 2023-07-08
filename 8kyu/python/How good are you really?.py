def better_than_average(class_points, your_points):
    res = 0
    for i in class_points:
        res+=i
    return True if your_points > res//len(class_points) else False
