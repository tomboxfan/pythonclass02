# The reason why Python is so powerful is because, Python has many built-in modules.
# All these modules come together, they form the standard library of Python


# IMPORTANT !!! ----------------------
# This is to important random module
# ------------------------------------
import random



# IMPORTANT !!! ----------------------------------------
# random.randint(1, 10) is composed of 4 parts
#
# 1) random     :  module name
# 2) .          :  separate module name and function name
# 3) randint    :  randint is a function.
#                  it is under random module
#                  it will return a random number in range [1, 10], both 1 and 10 are included. ('close interval')
#                  In math, we use [ and ] to express 'close interval'
#
# 4) (1, 10)    :  both 1 and 10 are arguments. They are surrounded by a pair of parenthesis
#                  What is argument? Argument is some value you pass to a function
# ------------------------------------------------------

i = 0
while i < 10:
    random_int = random.randint(1, 10) #random.randint(1, 10) returns a random int in range [1, 10]
    print(random_int)
    i += 1

print('-' * 20)

i = 0
while i < 10:
    random_number = random.random() # random.random() returns a random float value in range [0, 1); 0 is included, 1 is excluded (open interval)
    print(random_number)
    i += 1

# In math, we use ( and ) to express 'open interval'

print('-' * 20)

i = 0
while i < 10:
    random_number = random.uniform(1.2, 7.8) # random.uniform(1.2, 7.8) returns a random float in range [1.2, 7.8)
    print(random_number)
    i += 1