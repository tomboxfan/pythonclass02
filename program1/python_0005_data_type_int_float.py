
# int (integer)

# define a new variable h
h = 2 + 3   # 2 + 3 = 5, so variable h contains value 5

# define a new variable j, and I use the variable h
j = h - 100 # 5 - 100 = -95, so variable j contains value -95

k = h * j

print('variable h type is:', type(h), 'h=', h)
print('variable j type is:', type(j), 'j=', j)
print('variable k type is:', type(k), 'k=', k)

# type() is a python built-in function
# -------------------------------------------------
# What is a function?
#
# Function has a name - type
#
# Function has a pair of parentheses after the function name - type()
# Sometimes you can put a value / values inside the parentheses - type(h), print("hello")
#
# Function does something for you.
#    print("hello") is a function call. It helps you print "Hello" to the console.
#    type(h) is a function call.        It tells you the type of the variable h.
#
# What is python built-in function?
# The function is supplied / defined by Python.
# We will learn user-defined function in the future.
# -------------------------------------------------


# float - 小数
a = 1.2
b = 0.01
c = -12.0
d = a + b + c

# Ctrl + C -> Copy
# Ctrl + V -> Paste
print('variable a type is:', type(a), 'a=', a)
print('variable b type is:', type(b), 'b=', b)
print('variable c type is:', type(c), 'c=', c)
print('variable d type is:', type(d), 'd=', d)

# though both j and h are of type int, but j divided by h will give you a float e
e = j / h
print('variable e type is:', type(e), 'e=', e)
