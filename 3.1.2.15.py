c0= int(input('Input any non-negative and non-zero integer:'))
steps = 0
if c0 < 1 : print('Fuck off!')
else:
    print(c0)
    while c0 != 1:
        if c0%2 == 0:
            c0 /= 2
        else:
            c0 = 3 * c0 + 1
        steps += 1
        print(int(c0))
print('steps = ',steps)