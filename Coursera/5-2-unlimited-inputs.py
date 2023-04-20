largest = 0
smallest = None

while True :
    numS = input('Enter a number: ')
    if numS == 'done' :
        break
    try :
        numF = float(numS)
    except :
        print('Invalid input')
        continue

    if numF > largest :
        largest = numF
    if smallest is None :
        smallest = numF
    elif numF < smallest :
        smallest = numF
        
print('Maximum is', int(largest))
print('Minimum is', int(smallest))