# Whenever you define a variable
# No.1 question is: what's the type of the variable


# IMPORTANTCE! ------------------------------------------------------
# YOU MUST BE CRYSTAL CLEAR OF THE VARIABLE TYPE IN YOUR MIND
# -------------------------------------------------------------------
a_int_var = 1           # int, because it is natural number
a_float_var = 1.0       # float, because it has a decimal point
a_str_var = 'Hello'     # str, because it is surrounded by a pair of single quote of double quotes
a_bool_var = True       # bool, because bool has only 2 variales - True / False
# a_wrong_var = dog       # this is wrong

print(a_int_var, a_float_var, a_str_var, a_bool_var)
print(' -------------------------------------------------- ')

str_a = '10'    # this is of type 'str'
str_b = "10.2"  # this is of type 'str'

# if I plus 2 str variables together, I am actually joining them together
str_c = str_a + str_b # str + str -> str, so str_c is a str variable

print(f'Join 2 str: "{str_a}" + "{str_b}" = "{str_c}"')
print(' -------------------------------------------------- ')



# IMPORTANTCE! ---------------------------------------------------------------------------
# int()    - convert variable to a int variable    - it has a special name 'int constructor'
# float()  - convert variable to a float variable  - it has a special name 'float constructor'
# ----------------------------------------------------------------------------------------
int_a = int(str_a)              # convert str '10' to int 10
float_b = float(str_b)          # convert str '10.2' to float 10.2
print(f"{int_a}'s type is {type(int_a)}")          # 10's type is <class 'int'>
print(f"{float_b}'s type is {type(float_b)}")      # 10.2's type is <class 'float'>

# int_c = int("Hello") # ValueError: invalid literal for int() with base 10: 'Hello'
float_c = int_a + float_b   # int + float = float, so variable float_c is of type 'float'
print(f'Plus 2 numbers: {int_a} + {float_b} = {float_c}')  # Plus 2 numbers: 10 + 10.2 = 20.2

print(' -------------------------------------------------- ')


# More example of int constructor int() ---------------------------------

# IMPORTANTCE! ---------------------------------------------------------------------------
# When you pass a decimal value to the int constructor:
# It always tries shriking the decimal value to the nearest natural number towards 0
# It removes everything after the decimal points
# ----------------------------------------------------------------------------------------
int_a = int(2.1)    # 2
int_b = int(3.9)    # 3     not 4
int_c = int(-4.1)   # -4
int_d = int(-5.9)   # -5    not -6
int_e = int('6')    # 6
print(int_a, int_b, int_c, int_d, int_e) # 2 3 -4 -5 6

# More example of float constructor float() ------------------------------
float_a = float(2)
float_b = float(3)
float_c = float("4")
print(float_a, float_b, float_c) # 2.0 3.0 4.0