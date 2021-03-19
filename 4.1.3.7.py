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
   if month > 12: return None
   elif month < 8:
       if month % 2 == 1: return 31
       elif month == 2:
           if isYearLeap(year):
               return 29
           else:
               return 28
       else:
           return 30
   else:
       if month % 2 == 0: return 31
       else:
           return 30


testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")