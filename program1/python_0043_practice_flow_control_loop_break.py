# Requirement:
# Continuously get user input from console, ask user to input a number
# If the number is divisible by 7, then tell the user "The number is divisible by 7! Program exit!"
# Otherwise, ask user to try again.

'''
[Solution 1]
==================
Thinking Logic
==================
Convert a complex problem to a simple problem.


----------------------------------------------------
For all python programs, step 1) prepare 'data'
----------------------------------------------------
'''

'''
input_number = int(input("Please input a number: "))
if input_number % 7 == 0:
    print(f"{input_number} is divisible by 7! Program exit!")
    exit() # another python built-in function, this function will let you program exit immediately
else:
    print(f"{input_number} is NOT divisible by 7! Please try again!")
'''

# I use while True to let the program run time and time again

'''
while True:
    input_number = int(input("Please input a number: "))
    if input_number % 7 == 0:
        print(f"{input_number} is divisible by 7! Program exit!")
        break
    else:
        print(f"{input_number} is NOT divisible by 7! Please try again!")
'''

# [Solution 2]

remainder = 1

while remainder != 0:
    input_number = int(input("Please input a number: "))
    remainder = input_number % 7
    if remainder == 0:
        print(f"{input_number} is divisible by 7! Program exit!")
    else:
        print(f"{input_number} is NOT divisible by 7! Please try again!")