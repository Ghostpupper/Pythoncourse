def Exclamation_mark(numb):
    list1=[]
    for i in range(1,numb+1):
        list1.append(i)
        #4.print(list1)
    return sum(list1)

print(Exclamation_mark(int(input())))