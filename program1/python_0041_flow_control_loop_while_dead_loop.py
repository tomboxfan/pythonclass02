
# IMPORTANT!!! --------------------------------------
# This program will run forever, never exit.
#
# Because after keyword 'while', it is not a boolean expression, but a boolean value 'True'.
# There isn't any variable here, inside the loop body, we are not able to update the loop condition.
# So the loop will run forever.
#
# We call it 'dead loop'.
# As soon as Python code falls into this loop, Python code is dead. Looping forever, never comes out.
# ---------------------------------------------------

# while True:
#     print("I love Python!")



# Another example -----------------------
sheep_count = 0
while True:
    print(f"{sheep_count} sheep, I feel sleepy....")
    sheep_count += 1