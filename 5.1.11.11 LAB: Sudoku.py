sodukustring= """195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671"""
Result = True
def listify(list):
    templist = []
    for rad in list:
        templist.append([])
        for siffra in rad:
            siffra=int(siffra)
            templist[-1].append(siffra)
    return templist
def check_soduku(list):
    for number in list:
        list.remove(number)
        if number in list:
            return False
    return True

#input('input soduku: ')
rowlist= sodukustring.split('\n')
columnlist= 9*[""]
blocklist= [[],[],[],[],[],[],[],[],[],[]]
for row in rowlist:
    current_row= list(row)
    for i in range(len(rowlist)):
        string = columnlist[i]
        string += current_row[i]
        columnlist[i] = string

rowlist = listify(rowlist)
columnlist = listify(columnlist)

for row in rowlist:
    index = rowlist.index(row)
    for number in row:
        index2 = row.index(number)
        if index < 3:
            if index2 < 3:
                blocklist[0].append(number)
            elif index2>=3 and index2<6:
                blocklist[1].append(number)
            else:
                blocklist[2].append(number)
        elif index>=3 and index<6:
            if index2 < 3:
                blocklist[3].append(number)
            elif index2>=3 and index2<6:
                blocklist[4].append(number)
            else:
                blocklist[5].append(number)
        else:
            if index2 < 3:
                blocklist[6].append(number)
            elif index2>=3 and index2<6:
                blocklist[7].append(number)
            else:
                blocklist[8].append(number)

for row in rowlist:
    if check_soduku(row) == False:
        Result= False
for column in columnlist:
    if check_soduku(column) == False:
        Result= False
for block in blocklist:
    if check_soduku(block) == False:
        Result= False

if Result:
    print("it is a soduku")
else:
    print("its not a soduku")