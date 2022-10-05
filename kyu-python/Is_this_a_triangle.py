def is_triangle(a, b, c):
    output = None
    if a+b > c and a+c > b and b+c > a:
        output = True
    else:
        output = False
    return output
