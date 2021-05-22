year = int(input("Please input year: "))
month = int(input("Please input month (numerals) : "))
day = (input("Please input day (numerals) : "))

print(year, '-', month, '-', day)

user_input_month = input('Please input month (name of month) : ')

january = 0
february = 31
march = 31 + 28
april = 31 + 28 + 31
may = 31 + 28 + 31 + 30
june = 31 + 28 + 31 + 30 + 31
july = 31 + 28 + 31 + 30 + 31 + 30
august = 31 + 28 + 31 + 30 + 31 + 30 + 30
september = 31 + 28 + 31 + 30 + 31 + 30 + 30 + 31
october = 31 + 28 + 31 + 30 + 31 + 30 + 30 + 31 + 30
november = 31 + 28 + 31 + 30 + 31 + 30 + 30 + 31 + 30 + 31
december = 31 + 28 + 31 + 30 + 31 + 30 + 30 + 31 + 30 + 31 + 30

total_day_count = (user_input_month + day)

if user_input_month == january:
    print(f"{user_input_month} + {day} = {total_day_count}")
elif user_input_month == february:
    print(f"{user_input_month} + {day} = {total_day_count}")
elif user_input_month == march:
    print(f"{user_input_month} + {day} = {total_day_count}")
elif user_input_month == april:
    print(f"{user_input_month} + {day} = {total_day_count}")
elif user_input_month == may:
    print(f"{user_input_month} + {day} = {total_day_count}")
elif user_input_month == june:
    print(f"{user_input_month} + {day} = {total_day_count}")
elif user_input_month == july:
    print(f"{user_input_month} + {day} = {total_day_count}")
elif user_input_month == august:
    print(f"{user_input_month} + {day} = {total_day_count}")
elif user_input_month == september:
    print(f"{user_input_month} + {day} = {total_day_count}")
elif user_input_month == october:
    print(f"{user_input_month} + {day} = {total_day_count}")
elif user_input_month == november:
    print(f"{user_input_month} + {day} = {total_day_count}")
elif user_input_month == december:
    print(f"{user_input_month} + {day} = {total_day_count}")
else:
    print(f'Unrecognised month {user_input_month}')


is_leap_year = False

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    is_leap_year = True


# what you are going to do?
if is_leap_year:
    pass