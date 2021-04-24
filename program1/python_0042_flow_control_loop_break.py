a = 0
print("While loop starts:")

# IMPORTANT !!! ----------------------------------------------------
# 'break' will terminate the loop, very useful in a dead loop.
# 'break' will make your loop stop immediately and move on the next line of code.
# ------------------------------------------------------------------
while a < 5:
    a += 1
    if a == 3:
        break
    print(a)

print('While loop ends.')

# HOMEWORK:
# Refactor this counting sheep code, when counting sheep to 100, break out of the while loop.

sheep_count = 0
while True:
    print(f"{sheep_count} sheep, I feel sleepy....")
    sheep_count += 1
    if sheep_count > 100:
        break

# IMPORTANT !!! ------------------------------------------
# 'while True / break' combination very useful, very popular
# --------------------------------------------------------