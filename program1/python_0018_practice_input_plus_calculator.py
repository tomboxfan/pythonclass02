# Requirement: Implement a plus calculator

# int_a = input("Number a: ")
# int_b = input("Number b: ")
# result = int_a + int_b
# print(f"{int_a} + {int_b} = {result}")

# This is the homework for today
# You need to fix this program to make this plus calculator work properly

# Values returns from input function is of type 'str'
# '1' + '2' = '12' -> plus sign joins 2 str values together
# To fix this, you need to convert the 2 variables to type 'int'
# 1 + 2 = 3

int_a = int(input("Number a:"))
int_b = int(input("Number b:"))
result = int_a + int_b
print(f"{int_a} + {int_b} = {result}")