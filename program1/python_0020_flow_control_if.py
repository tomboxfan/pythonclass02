# Every python code you have seen so far is sequential execution.
# Code is executed strictly line after line, from top to bottom.

# Flow control can help you
# 1) skip over some lines of code.
# 2) choose between alternative code.


# Flow control - if statement

# example 1 simple if -----------------------------------
today = input("What day is today? ")

print("I get up at 7 am.")
print("I have my breakfast at 8 am.")



# IMPORTANTCE !!!----------------------------------------
#
# if <boolean expression>:
#     <statement>
#     <statement>
#     <statement>
#
# 1) ":" at the end of the if clause
# 2) All code under if section are indented 4 spaces.
# 3) Treat the 3 pinrt statements as a 'block'.
#    The 'block' will be executed if today = 'Sunday' is True, otherwise, the 'block' won't get executed.
# -------------------------------------------------------
if today == 'Sunday': # today == 'Sunday' is a boolean expression, the boolean expression will always give you a boolean value - True / False
    print("I attend Math tuition lesson at 9 am.")
    print("I start working on my tuition homework at 10:30 am.")
    print("Tuition homework is done at 11:30 am.")


print("I have my lunch at 12 am.")
print("I play football with my friends at 5 pm.")
print("I have my dinner at 7 pm.")
print("I go to bed at 10 pm.")
