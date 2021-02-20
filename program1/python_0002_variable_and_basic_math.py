
# The most important thing in Python program is:
# 1) Define a variable
# 2) Use a variable


# This is define a variable
# I can give the variable name what I like
# I want to give my variable a name -> a_number, and I want to put value 5 into variable a_number's box.
a_number = 5


# I want to give my variable a name -> another_number, and I want to put value 2 into variable another_number's box.
another_number = 2


greeting_word = 'Hello!' # the value is surrounded by single quote, this means it is str type.


print(a_number, another_number, greeting_word)


# This is using variable a_number and another_number
# This is also defining a new variable - plus_variable
plus_variable = a_number + another_number
minus_variable = a_number - another_number
divide_variable = a_number / another_number
mutiply_variable = a_number * another_number

#Floor Division - find quotient
divide_variable2 = a_number // another_number   # 5 // 2 = 2 (quotient)  5 divided by 2 = 2r1

# Modulus - find remainder
remainder_variable = a_number % another_number # 5 % 2 = 1 (remainder)


# Exponentiation
# 5 ** 2 = 25   -> 5 * 5 = 25
# 5 ** 3 = 125  -> 5 * 5 * 5 = 125
# 5 ** 4 = 625  -> 5 * 5 * 5 * 5 = 625
power_variable = a_number ** another_number     # 25
power_variable2 = power_variable ** (1/2)       # 5



# 'Control + /' will make the line a comment, or vice versa.
# print(plus_variable, minus_variable, divide_variable, mutiply_variable)


print(a_number, '+', another_number, '=', plus_variable)
print(a_number, '-', another_number, '=', minus_variable)
print(a_number, '/', another_number, '=', divide_variable)
print(a_number, '*', another_number, '=', mutiply_variable)
print(a_number, '//', another_number, '=', divide_variable2)
print(a_number, '%', another_number, '=', remainder_variable)
print(a_number, '**', another_number, '=', power_variable) # int type
print(power_variable, '** (1/2)', '=', power_variable2) # float type


# Step 1) define variables a/b/c/d/e/f
a = 1
b = 2
c = 5
d = 6
e = 7
f = 9

# Step 2) doing math using variables a/b/c/d/e/f, assign the result to a newly-defined variable 'answer'
answer = (a - (a / b) * (b / c)) / (e / f)

# Step 3) user variable answer
print(answer)