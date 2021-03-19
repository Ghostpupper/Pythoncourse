myList = [3,4,2,3,5,6,7,8,1,2,4,5,5,6,1,0,7,6,6,6,6,4,31,3,0]
templist = []

for i in myList:
    if i not in templist:
        templist.append(i)
        print(templist)

myList= templist[:]
myList.sort()

#
# put your code here
#
print("The list with unique elements only:")
print(myList)