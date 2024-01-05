# A simple calculator

number1 = int(input('Enter a number: '))
number2 = int(input('Enter another number: '))
print('+--------------------+')
print('|  + or - or / or *  |')
print('+--------------------+')
ops = input('Enter the operation: ')

def sum(a, b):
    print('The addition is: ', a + b)
def sub(a, b):
    print('The subtraction is: ', a - b)
def mul(a, b):
    print('The multiplication is: ', a * b)
def div(a, b):
    print('The division is: ', a / b)

if ops == '+':
    sum(number1, number2)
elif ops == '-':
    sub(number1, number2)
elif ops == '/':
    div(number1, number2)
elif ops == '*':
    mul(number1, number2)
else:
    print('Invalid input.')
