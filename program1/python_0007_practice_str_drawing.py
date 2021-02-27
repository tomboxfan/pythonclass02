# Requirement: I want to print a square with length = 5

# Example 1)
# Let's print a small square 2 * 2
star_line = '*' * 2
print(star_line)
print(star_line)

print("---------------------------------------------------------")

star_line = '*' * 5
print(star_line)
print(star_line)
print(star_line)
print(star_line)
print(star_line)

print("---------------------------------------------------------")

# I want to move the square to the centre. So,
star_line = ' ' * 5 + '*' * 5
print(star_line)
print(star_line)
print(star_line)
print(star_line)
print(star_line)

print("---------------------------------------------------------")

# I want to print a hollow square

# Between the upper border and lower border, each line is
# 1) 5 ' ' in the left.
# 2) 1 '*' (left border), (5 - 2) spaces, and 1 '*' (right border)
# How many rows should I print? 5 - 2 = 3

left_star_right_star = ' ' * 5 + '*' + ' ' * 3 + '*'

print(star_line)
print(left_star_right_star)
print(left_star_right_star)
print(left_star_right_star)
print(star_line)


print("---------------------------------------------------------")
# Letter 'P'
# Total height: 7 lines

left_star = ' ' * 5 + '*' + ' ' * 4

print(star_line)
print(left_star_right_star)
print(left_star_right_star)
print(star_line)
print(left_star)
print(left_star)
print(left_star)

print("---------------------------------------------------------")
# Letter 'Y'

right_star = ' ' * 9 + '*'

print(left_star_right_star)
print(left_star_right_star)
print(left_star_right_star)
print(star_line)
print(right_star)
print(right_star)
print(star_line)

