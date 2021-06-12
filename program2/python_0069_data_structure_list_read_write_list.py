fruits = ['Apple', 'Orange', 'Banana', "Pear"]
animals = ['tiger', 'elephant', 'snake', 'shark']



# --------------------------
# READ item value from list
# --------------------------
# visit the value inside the cabinet

# Solution 1: use square bracket
print(animals[0], 'is at index 0') # tiger
print(animals[-1], 'is at index -1') # shark

print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

# Solution 2: use for loop
for animal in animals:
    print(animal, end=' ')
print("\n-----------------------------------")


# --------------------------
# READ item index from list
# --------------------------

# use index() method
print("'tiger's index is", animals.index('tiger')) # 0
print("'shark's index is", animals.index('shark')) # 3

print("\n-----------------------------------")

# --------------------------
# READ item index/ value from list
# --------------------------

# Solution 1
index = 0
for animal in animals:
    print(f"{index} : {animal}")
    index += 1
# We don't code in this way, we have another built-in function - enumerate(list)

# Solution 2 (better): use built-in function enumerate(list)
for index, animal in enumerate(animals):
    print(f"{index} : {animal}")

# IMPORTANCE !!! ------------------------------------------------------------
# built-in function: enumerate(list) combines index and value into a group
# ---------------------------------------------------------------------------

print("\n-----------------------------------")

# ------------------------------------------
# WRITE to list
# 'WRITE' means 'change' / 'update' value inside the list
# -----------------------------------------

# Solution 1: change / update item value to list
animals[0] = 'tiger'
print(animals)

fruits[1] = 'Durian'
print(fruits)

# IMPORTANCE !!!! ----------------------------
# You can change the content of a list.
# Remember: list is MUTABLE
# --------------------------------------------





