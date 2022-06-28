import calendar

# dec = calendar.TextCalendar(calendar.SUNDAY)
# dec.prmonth(2020, 12)


month_day_year = input("Enter date press shift, Enter month press shift and Enter year. Then press enter. \n")
month_day_year = month_day_year.split()

month = int(month_day_year[0])
day = int(month_day_year[1])
year = int(month_day_year[2])

cal = calendar.weekday(year, month, day)


if cal == 0:
    print("MONDAY")

elif cal == 1:
    print("TUESDAY")  

elif cal == 2:
    print("WEDNESDAY") 

elif cal == 3:
    print("THURSDAY")   

elif cal == 4:
    print("FRIDAY")  

elif cal == 5:
    print("SATURDAY") 

elif cal == 6:
    print("SUNDAY")


# print("============================================")
# print(">>>>>>>>>>>> LEAP YEAR CALCULATOR <<<<<<<<<<<")
# year1 = int(input("Enter the first year: "))
# year2 = int(input("Enter the second year: "))

# leaps = calendar.leapdays(year1, year2)
# print(f"Number of years between {year1} and {year2} is: {leaps} years" )
# print("=============================================")


# year = int(input("Enter the year to display: "))
# print(calendar.prcal(year))


# cal = calendar.TextCalendar(calendar.SUNDAY)
# for i in cal.itermonthdays(2002, 1):
#     print(i)


# print("MOTHS OF THE YEAR ARE:")
# for name in calendar.month_name:
#     print(name, "\n")

# print("DAYS OF THE WEEK ARE")   
# for name in calendar.day_name:
#     print(name, "\n")


# with open("C:/Users/user/student-result/hackerrank/calendar.html", "w") as cal:
#     c = calendar.HTMLCalendar(calendar.SUNDAY)
#     cal.write(c.formatmonth(2020, 12))