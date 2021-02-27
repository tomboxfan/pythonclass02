# bool is the 4th data type in python
# it has only 2 values. True and False
# It represents something True or False
# For example: is today a Sunny day? True
# For example: is today Tuesday? False

# Step 1) define variables
bool1 = True
bool2 = False

print('Variable bool1 type is:', type(bool1), 'bool1=', bool1)
print('Variable bool2 type is:', type(bool2), 'bool2=', bool2)



# You can compare 2 values and you get a True/False result. And the result is assigned to a variable.
# And the variable has a type 'bool'.
# It is separated by '=', on the left is the variable name, on the right is a 'boolean expression'.

# What is a boolean expression?
# 1 > 2 is a boolean expression, and the result is False
# 100 < 200 is another boolean expression, and the result is True
bool3 = (1 > 2)  # 1 > 2 is False. variable bool3 is assigned a bool value - False
bool4 = (100 < 200) # 100 < 200 is True, variable bool4 is assigned a bool value - True

print('Variable bool3 type is:', type(bool3), 'bool3=', bool3)
print('Variable bool4 type is:', type(bool4), 'bool4=', bool4)
