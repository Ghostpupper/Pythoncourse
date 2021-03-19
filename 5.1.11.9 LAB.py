lifestring = input("Write your birthday in YYYYMMDD format. ")


def makelife(string):
    total = 0
    for letter in string:
        total += int(letter)
    return total

if lifestring.isdigit():
    total = str(makelife(lifestring))
    total= makelife(total)
    print(total)
else:
    print("not valid value")