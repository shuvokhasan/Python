# Takes a value, checks weather odd or even

num = int(input('Enter a value: '))

if num == 0:
    print('The number is zero')
elif num % 2 == 0:
    print('The number is Even.')
elif num % 2 != 0:
    print('The number is Odd.')

exit()