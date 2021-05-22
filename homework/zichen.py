'''
Requirement:
user inputs year / month / day information from the console
Your program needs to tell the user how many days in the year there are in front of the date which user input
For example: if user tells you 2019 Jan 1st, then your output should be 1
For example: if user tells you 2019 Feb 1st, then your output should be 32
HINT: Please consider leap year.
'''

year = int(input("Please input year:"))
month = int(input("Please input month:"))
day = int(input("Please input day:"))

print(year, '-', month, '-', day)
Jan = 31
Feb = 59
Mar = 90
Apr = 120
May = 151
Jun = 181
Jul = 212
Aug = 243
Sep = 273
Oct = 304
Nov = 334
Dec = 356


# You should code in this way:
days_passed = 0

if month == 2:
    days_passed = Jan   #if it is Feb, you need to add 31 days to days_pass
elif month == 3:
    days_passed = Feb
elif month == 4:
    days_passed = Mar


print(days_passed)