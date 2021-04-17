'''
Babylonian square-root algorithm is very famous!
中文叫作巴比伦算法
Here it is how it works to calculate the square root of any number x:

Step 1) define variable a = 1
Step 2) define variable b = x / a

Step 3) assign variable a = (a + b) / 2     -   Now a stands in the mid point of a and b. This is to move a closer to b
Step 4) assign variable b = x / a

Because square_root * square_root = x; so a and b, one is smaller than square_root, another is bigger than square_root
We move a to the mid point between a and b, so we make a closer to the square_root
because a * b = x, if a is closer to the square_root, b is also closer to the square_root


Step 5) assign variable a = (a + b) / 2
Step 6) assign variable b = x / a

Step 7) assign variable a = (a + b) / 2
Step 8) assign variable b = x / a

repeat..repeat..

until a and b are close enough, say b - a < 0.000000000001
Then a is equal to b (almost)
Then a or b is the square root of x


Example:
Let's calculate the square root of 25
a = 1
b = 25 / 1 = 25

a = (1 + 25) / 2 = 13             b = 25 / 13 = 1.923             diff = 11.077
a = (13 + 1.923) / 2 = 7.462      b = 25 / 7.462 = 3.351          diff = 4.111
a = (7.462 + 3.351) / 2 = 5.406   b = 25 / 5.406 = 4.624          diff = 0.782
... ...

'''

# Step 1) Prepare the data ---------------------------

# x is number which we need to calculate the square root
x = int(input("Number: "))

# a starts from 1
a = 1

# b starts from x / 1, which is x
b = x / a

# actual_diff is the distance between a and b
actual_diff = b - a

print(f"a:{a}, b:{b}, actual_diff: {actual_diff}")


target_diff = 0.000000000001

# Step 2) Our program starts ------------------------

while actual_diff > target_diff:

    a = (a + b) / 2
    b = x / a

    actual_diff = abs(a - b) # last step is to update the loop condition
    print(f"a:{a:.3f}, b:{b:.3f}, actual_diff: {actual_diff:.3f}")

print(f'Square root of {x} is: {a:.3f}')
print(f'{a:.3f} * {a:.3f} = {a ** 2:.3f}')

# SUMMARY ----------------------------------
# a) while loop always start with keyword 'while'
#
# b) after keyword 'while', we use a boolean expression.
#    This boolean expression tell us when our program stops running the loop.
#    When it is True, is continues looping.
#    When it is False, it stops looping.
#
# c) The boolean expression involes some variables ( actual_diff / target_diff).
#    Inside the while loop body, the variable value should be changed, meaning loop condition is updated, meaning while loop has a opportunity to stop.
#    So each time an iteration finishes, Python will check, 'is the boolean expression still True?'
# -------------------------------------------