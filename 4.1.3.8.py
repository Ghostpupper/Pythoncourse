def isYearLeap(year):
    if year < 1582:
        return None
    else:
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        elif year % 400 != 0:
            return False
        else:
            return True

def daysInMonth(year, month):
    if month > 12:
        return None
    elif month < 8:
        if month % 2 == 1:
            return 31
        elif month == 2:
            if isYearLeap(year):
                return 29
            else:
                return 28
        else:
            return 30
    else:
        if month % 2 == 0:
            return 31
        else:
            return 30

def dayOfYear(year, month, day):
    days=0
    for i in range(1,month):
        days += daysInMonth(year,   i)
    days += day
    return days

print(dayOfYear(2000, 12, 31))