def update_light(current):
    result =''
    if current =='green':
        result = 'yellow'
    elif current == 'yellow':
        result = 'red'
    else:
        result = 'green'
    return result

