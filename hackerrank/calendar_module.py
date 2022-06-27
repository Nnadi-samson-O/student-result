import calendar

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