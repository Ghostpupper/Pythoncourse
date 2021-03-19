string1 = input("word 1: ")
string2 = input("word 2: ")
res= False
max= len(string2)
"""counter2 = 0
for letter in list1:
    res= True
    while counter2 < max:
        letter2= string2[counter2]
        if letter == letter2:
            counter2 += 1
            break
        else:
            counter2 += 1
            continue
    else:
        res= False
        break
if res:
     print('Yes')
else:
    print('No') """
def findword(string1, string2):
    list1 = list(string1)
    list2 = list(string2)
    counter1=0
    counter2 = 0
    while counter2 < max:
        value = string2.find(list1[counter1],counter2, max)
        if value == -1:
            return False
        else:
            counter2= value
            counter1 += 1
            if counter1 >= len(string1):
                return True
            continue

    return True

if findword(string1, string2):
    print('Yes')
else:
    print('No')




