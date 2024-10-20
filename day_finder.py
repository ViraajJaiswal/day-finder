#WAP to accept 2 dates in DD/MM/YY and the day on date 1, and find the day on date 2

date1 = str(input("Enter the first date ")+" ")
d1 = int(date1[0:2])
m1 = int(date1[3:5])
y1 = int(date1[6:8])

day = str(input("Enter the day of the date")) #day of date1

date2 = str(input("Enter the second date"))
d2 = int(date2[0:2])
m2 = int(date2[3:5])
y2 = int(date2[6:8])

dayno = [31,28,31,30,31,30,31,31,30,31,30,31] #no of days in every month of the year
dayna = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"] #name of days of the week

din = dayna.index(day) #index of the day of date1 in the list of day names

td1 = 0 #total no of days in date 1
for i in range(m1):
    td1 += dayno[i]
td1 += d1 + (365 * y1) + (y1 // 4) - (y1 // 100) + (y1 // 400) #days in no of years of date1 (including leap years)

td2 = 0 #total no of days in date 2
for i in range(m2):
    td2 += dayno[i]
td2 += d2 + (365 * y2) + (y2 // 4) - (y2 // 100) + (y2 // 400) #days in no of years of date2 (including leap years)

ddif = td2-td1 #difference of days between the two dates
solin = din + (ddif%7) #index of day of date2

if(solin<7):
    print("The day on the second date is "+dayna[solin])
elif(solin>6):
    solin = solin-7
    print("The day on the second date is "+dayna[solin])
