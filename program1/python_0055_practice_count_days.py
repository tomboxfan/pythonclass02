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

total_day = 0

#-------------------------------------------------------
# Finish your homework here
# ... ...







is_leap_year = False

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    is_leap_year = True


# what you are going to do?
if is_leap_year:
    pass





