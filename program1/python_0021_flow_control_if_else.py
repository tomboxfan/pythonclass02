

# IMPORTANTCE !!!----------------------------------------
#
# if <boolean expression>:
#     <statement>
#     <statement>
# else:
#     <statement>
#     <statement>
#
# 1) ":" at the end of the else clause as well
# 2) all code under else block are indented 4 spaces as well
# 3) Tread the 2 print statements under if clause as a 'block'.
#    The 'block' will be executed only if years_learning_python > 5 is True
# 4) Tread the 3 print statements under else clause as a 'block'.
#    The 'block' will be executed only if years_learning_python > 5 is False
# -------------------------------------------------------

years_learning_python = int(input("How many years have you been learning Python? "))

if years_learning_python > 5:
    print(f"Not bad! {years_learning_python} years is quite a long time, you've already been a Python Guru!")
    print("I am sure you can earn a lot of money in the market!")
else:
    print(f"{years_learning_python} years is still quite short.")
    print("I know it is hard, just hang in there! Not everybody has the opportunity to learn Python!")
    print("You are really lucky!")

print("Python is the future! You are on the right track!")