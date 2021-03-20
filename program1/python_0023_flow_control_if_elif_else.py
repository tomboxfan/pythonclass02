'''
Requirement: base on user input age, and tell whether the current user is a adult? a teenager? a kid? Or a baby?
'''

# IMPORTANTCE !! -------------------------------------------------
# if / elif / else gives you multiple choices.
# You pick one path.
# ----------------------------------------------------------------

age = int(input("How old are you? "))

if age >= 20:                                                   # Test Expression 1
    print("You are an adult now")                               # Statement 1
    print("You can start a software programmer career!")        # Statement 2
elif age >= 13:                                                 # Test Expression 2
    print("You are still a teenager")                           # Statement 3
    print("You should start taking some Python lesson")         # Statement 4
elif age >= 3:                                                  # Test Expression 3
    print("You are still a kid")                                # Statement 5
    print("Play time at your age! Enjoy!")                      # Statement 6
else:
    print("You are still a baby")                               # Body of Else - Statement 7
    print("Eating, Drinking, Sleeping, Pooping, Crying...")     # Body of Else - Statement 8

print(f"You are {age} years old.")