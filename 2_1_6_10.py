x = float(input("Enter value for x: "))

y = (x + x**-1)
y **= -1
y += x
y **= -1
y += x
y **= -1

print("y =", y)
