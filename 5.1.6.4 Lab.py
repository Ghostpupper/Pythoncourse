def readint(prompt, min, max):
    while True:
        value = input(prompt)
        try:
            value = int(value)
            assert value >= min
            assert value <= max
        except ValueError:
            print("Error: Wrong Input")
            continue
        except AssertionError:
            print("Error: the value is not within permitted range (",min,"..",max,")",sep="",end="\n")
            continue
        except KeyboardInterrupt:
            print("You are free now")
            break
        return value


#
# put your code here
#

v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)