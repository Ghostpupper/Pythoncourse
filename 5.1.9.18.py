def myremovespaces(strng):
    newstrng = ""
    for letter in strng:
        if letter != " ":
            newstrng += letter

    return newstrng

def mysplit(strng):
    newstring = strng.lstrip()
    list = []
    item= ""
    while True:
        try:
            sep_pos = newstring.index(" ")
            for i in range(sep_pos):

                item += newstring[i]
            list.append(item)
            newstring = newstring.lstrip(item)
            newstring = newstring.lstrip()
            item= ""
        except ValueError:
            break
    return list


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))