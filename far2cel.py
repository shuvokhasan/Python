# Farenheit to Celcius conversion

def toCelcius(farenheit):
    farenheit = float(inp)
    celcius = (farenheit - 32.00) * (5.00 / 9.00)
    return celcius

try:
    inp = input('Enter Farenheit value: ')
    print(toCelcius(inp))

except:
    print('Enter a valid number.')
    inp = input('Enter Farenheit value: ')
    print(toCelcius(inp))