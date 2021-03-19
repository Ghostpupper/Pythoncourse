def LedDisplay(numbers):

    snumbers = str(numbers)
    lnumbers = list(snumbers)
    for i in range(5):
        for j in lnumbers:
            numj = int(j)
            if i == 0:
                if numj == 1:
                    print('  #',sep='',end=' ')
                elif numj == 4:
                    print('# #',sep='',end=' ')
                else:
                    print('###',end= ' ')
            if i == 1:
                if numj == 5 or numj == 6:
                    print('#  ',sep='',end=' ')
                elif numj == 4 or numj == 9 or numj == 8:
                    print('# #',sep='',end=' ')
                else:
                    print('  #',end=' ')
            if i == 2:
                if numj == 1 or numj == 7:
                    print('  #',end=' ')
                else:
                    print('###',end=' ')
            if i == 3:
                if numj== 8 or numj == 6:
                    print('# #',end=' ')
                elif numj==2:
                    print('#  ', end=' ')
                else:
                    print('  #',end=' ')
            if i  == 4:
                if numj==1 or numj==7 or numj== 4 or numj==9:
                    print('  #',end=' ')
                else:
                    print('###',end=' ')
            print(' ',sep='',end='')
        print('')

LedDisplay(int(input()))