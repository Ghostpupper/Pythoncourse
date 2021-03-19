hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
"""Hey
I think youre really cool
I like you a lot
im thinking we should
hangout or something"""
totalmins = dura + mins
extrahours = int(totalmins/60)
resulthours = (hour + extrahours)%24
resultmins = totalmins%60

print(resulthours,":",resultmins)
