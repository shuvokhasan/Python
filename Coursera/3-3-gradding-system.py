scoreS = input("Enter Score: ")

try: 
    scoreF = float(scoreS)

except:
    print('Error, please enter numeric value.')

if scoreF >= 0.9 and scoreF <= 1.0 :
    print('A')
elif scoreF >= 0.8 and scoreF < 0.9 :
    print('B')
elif scoreF >= 0.7 and scoreF < 0.8 :
    print('C')
elif scoreF >= 0.6 and scoreF < 0.7 :
    print('D')
elif scoreF < 0.6 and scoreF <= 0.0 :
    print('F')
else :
    print('Please enter point between 0.00 to 1.00')