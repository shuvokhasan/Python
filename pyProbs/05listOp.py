numbers = [5, 10, 3, 8, 15]

count = 0
for number in numbers:
    count = count + 1
print('The array has', count, 'items.')

sum = 0
for item in numbers:
    sum = sum + item
print('The sum is: ', sum)

max = 0
min = 0
for num in range(len(numbers)):
    count = count + 1
    if numbers[count] < numbers[count + 1]:
        max = numbers[count + 1]
    else: numbers[count]