'''
Requirement:
Redo 0055 Using list

Requirement of 0055:
user inputs year / month / day information from the console
Your program needs to tell the user how many days in the year there are in front of the date which user input
For example: if user tells you 2019 Jan 1st, then your output should be 1
For example: if user tells you 2019 Feb 1st, then your output should be 32
'''

'''
Logic is the most important! When the logic is clear, then we convert the logic to code:

-Core Logic -------------------------
Observation:
For each date which user has typed in the console, there are always fixed number of full months in front the date.
For example:
There are always 4 full months in any date in May.
There are always 8 full months in any date in Sep.

Conclusion:
I can build a list - dayList, which contains 12 values. And these 12 values map Jan / Feb ... Dec.
Each value stands for the total days' count for those full months in front of the date.

dayList[0] = 0   # There are 0 days in those full months in front of any Jan date.
dayList[1] = 31  # There are 31 days in those full months in front of any Feb date.
dayList[2] = 31 + 28  # There are 31 + 28 days in those full months(Jan/Feb) in front of any Mar date. (Let's ignore leap year for now)
... ...
dayList[11] = ... ... 
'''


year = int(input("Please input year:"))
month = int(input("Please input month:"))
day = int(input("Please input day:"))

print(year, '-', month, '-', day)

dayList = [ 0,          # There are 0 days in those full months in front of any Jan date.
            31,         # There are 31 days in those full months in front of any Feb date.
            31 + 28,    # There are 31 + 28 days in those full months(Jan/Feb) in front of any Mar date. (Let's ignore leap year for now)
            31 + 28 + 31, # Apr
            31 + 28 + 31 + 30, # May
            31 + 28 + 31 + 30 + 31, # Jun
            31 + 28 + 31 + 30 + 31 + 30, # Jul
            31 + 28 + 31 + 30 + 31 + 30 + 31, # Aug
            31 + 28 + 31 + 30 + 31 + 30 + 31 + 31, # Sep
            31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30, # Oct
            31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31, # Nov
            31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 # Dec
]

total_days = dayList[month - 1] # list index starts from 0. So for Jan (month = 1), I should use daysList[0]; for Feb (month = 2), I should use daysList[1];
total_days += day


# Check leap year --------------------------------------------
is_leap_year = False

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    is_leap_year = True

if is_leap_year and month > 2:
    total_days += 1
# ------------------------------------------------------------


print("Today days:", total_days)

