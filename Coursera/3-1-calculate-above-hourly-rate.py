hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

if h > 40 :
    overTime = h - 40
    payOverTime = (overTime * (r * 1.5))

    flatPayTime = h - overTime
    flatPay = flatPayTime * r

    grossPay = payOverTime + flatPay
else :
    grossPay = h * r

print(grossPay)