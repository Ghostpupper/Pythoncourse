"""# read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
same_number = False
# choose the larger number
if number1 > number2: larger_number = number1
elif number1 == number2: same_number = True
else: larger_number = number2

# print the result
if same_number: print("Those are the same number you idiot! ")
else: print("The larger number is:", larger_number)"""

blomma = input("Gimme a flower! \n")

if blomma == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif blomma == "spatiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not ",blomma,"!",sep = "")