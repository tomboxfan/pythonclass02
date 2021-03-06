first_name = 'James'
last_name = "Bond"

# Requirement: Print out str 'My name is Bond, James Bond' using variables first_name and last_name

# [solution 1] pass 5 str values to print() function
# Problem: there is an extra space between Bond and ','
print('My name is', last_name, ',', first_name, last_name)

# [solution 2] Use '+' sign to join 6 str values together, pass this newly-joined str value to print() function
# Problem: Too many '+' sign, very messy, not readable.
print('My name is ' + last_name + ', ' + first_name + ' ' + last_name)

# [solution 3] Use python f string
# IMPORTANCE!!! ---------------------------------------------------------------------------
# 1) Have an f at the beginning
# 2) curly braces containing expressions / variables that will be replaced with their values.
# -----------------------------------------------------------------------------------------
print(f'My name is {last_name}, {first_name} {last_name}')


# More examples:
print(f'No. Mr {last_name}, I expect you to die!')

age = 91
print(f'Sean Connery is now {age} years old')

language = 'JavaScript'
rank = 1
who = 'all kids'
kids_age = 12
teacher_surname = 'FAN'

print(f'{language} is the world no {rank} programming language, {who} should start learning it from age {kids_age}, and they all learn {language} with Teacher {teacher_surname}.')
print(f'{who} enjoy learning {language}, as {language} is quite fun, and Teacher {teacher_surname} is quite fun!')

# IMPORTANCE!!! --------------------------------------------------------------------------------------------------
# Benefit:
# 1) Same variable can be used multiple times.
# 2) Once you replace the variable value, then the whole content get changed whereever the variable is referenced.
# ----------------------------------------------------------------------------------------------------------------