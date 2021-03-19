
years = [int(input("Enter a year: ")), int(input("and another: "))]

for year in years:

    if year < 1582: print('Not within the Gregorian calendar period')
    else:
        if year%4 != 0: print("Common year")
        elif year%100 != 0: print("Leap year")
        elif year%400 != 0: print("common year")
        else: print("Leap Year")
