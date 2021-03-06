# example 1)

# Step 1) define a variable
toms_age = 20

# Step 2) Use variable toms_age
# ==    tells you whether the number on the left and right are equal or not
# =     assigns value on the right to the variable on the left
#       'toms_age == 20' is a boolean expression, and its value equals to True
print("Is Tom 20 years old? ", toms_age == 20)

# 'toms_age == 13', its value is False
print("Is Tom 13 years old? ", toms_age == 13)

# 'toms_age != 20', its value is False
print("Tom is not 20 years old. Right? ", toms_age != 20)


a = (toms_age == 20) # toms_age == 20 equals to True, so variable a equals to True
b = (toms_age == 13) # toms_age == 13 equals to False, so variable b equals to False
c = (toms_age != 20) # variable c equals to False
d = (toms_age != 13) # variable d equals to True
e = (toms_age < 30) # variable e equals to True
f = (toms_age <= 20) # variable f equals to True
g = (toms_age > 30) # variable f equals to False
h = (toms_age >= 30) # variable h equals to False
print(a,b,c,d,e,f,g,h) # True False False True True True False False


# assign operator(=) has a lower priority then the 6 rational operators( >  <  >=  <=  !=  ==)
a = toms_age == 20

# Example 2)

my_math_mark = 75
is_my_math_excellent = (my_math_mark > 90)
print("Is my math excellent? ", is_my_math_excellent)

have_i_failed_in_math = (my_math_mark < 60)
print("Have I failed in Math? ", have_i_failed_in_math)

billy_math_mark = 75
does_billy_have_same_score_as_mine = (my_math_mark == billy_math_mark)
print("Does Billy have same score as mine? ", does_billy_have_same_score_as_mine)