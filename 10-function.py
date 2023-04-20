def greeting() :
    return 'Good Morning'

def greet(time) :
    if time == 'morning' :
        return 'morning'
    elif time == 'noon' :
        return 'noon'
    elif time == 'evening' :
        return 'evening'
    elif time == 'night' :
        return 'night'
    else :
        return 'Please enter valid time'

print('Good', greet('morning'), 'Shuvo')

