def computepay(h, r) :
    return h * r

h = float(input('Enter Hours: '))
r = float(input('Enter Rate: '))

if h > 40 :
    overtime = h - 40
    grossPay = (computepay(40, r) + computepay(overtime, (1.5 * r)))
else :
    grossPay = computepay(h, r)

print('Pay', grossPay)