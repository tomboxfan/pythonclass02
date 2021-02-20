# define a variable with value 5
h = 5
print("Now h value is", h)



# A very interesting example ------------------
# Assign a new value to variable h, using h's old value.
# h's old value is 5
# 5 - 1 = 4
# Assign 4 back to variable h
# Now h contains a new value 4
# Control + y -> delete the current line
h = h - 1
print("Now h value is", h)  # 4

h -= 1  # this equals to h = h - 1
print("Now h value is", h)  # 3

h += 1  # this equals to h = h + 1
print("Now h value is", h)  # 4

h *= 2
print("Now h value is", h) # 8

h /= 4
print("Now h value is", h) # 2

