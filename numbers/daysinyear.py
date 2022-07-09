# python program to find no of days in a year

def is_leap(year):
    if year%400 ==0 or (year%4 == 0 and year%100 != 0):
        return True
    return False

def daysInMonth(year,month):
    if month == 2 and is_leap(year):
        return "No of days is 29"
    elif month == 2:
        return "No of days is 28"
    elif month==1 or month==3 or month== 5 or month==7 or month==8 or month==10 or month==12:
        return "No of days is 31"
    else:
        return "No of days is 30"
        

year = int(input("Please enter a year: "))
month = int(input("Please enter the month number: "))
print(daysInMonth(year, month))