animals = ['tiger', 'elephant', 'snake', 'shark'] * 2
print(animals) # ['tiger', 'elephant', 'snake', 'shark', 'tiger', 'elephant', 'snake', 'shark']

# Solution 1: use del - remove item by index
del animals[1]
print(animals) # ['tiger', 'snake', 'shark', 'tiger', 'elephant', 'snake', 'shark']


# Solution 2: Use pop - remove item by index
popped_animal = animals.pop()
print(popped_animal, 'is popped out.') # shark is popped out.
print(animals) # ['tiger', 'snake', 'shark', 'tiger', 'elephant', 'snake']

popped_animal = animals.pop(1)
print(popped_animal, 'at index 1 is popped out.') # snake at index 1 is popped out.
print(animals) # ['tiger', 'shark', 'tiger', 'elephant', 'snake']

# index must be a valid value, otherwise:
# IndexError: pop index out of range
# popped_animal = animals.pop(20)

# So you need to check index before calling pop method
index = 20
if index < len(animals):
    popped_animal = animals.pop(index)
else:
    print(f"{index} is an invalid index value of list animals, right now we only have {len(animals)} items in animals.")
# IMPORTANCE !!! ---------------------------------------------
# bulit-in function len(list_a) tells you the size of list_a
# ------------------------------------------------------------


# Solution 3: Use remove - remove item by value
animals.remove('tiger')
print(animals) # ['shark', 'tiger', 'elephant', 'snake']
# remove(value) will only remove the 1st matched item, and ignore all the following matched items.


# ValueError: list.remove(x): x not in list
# animals.remove("leopard")

if 'leopard' in animals:
    animals.remove("leopard")
else:
    print("'leopard' doesn't exist in list animals")

if 'penguine' not in animals:
    animals.append("penguine")
    print("'penguine' has been appended to animals")
    print(animals)

# IMPORTANCE !!! ---------------------------------------------------------
# 'in' operator tells us whether the item exists in the list or not
# ------------------------------------------------------------------------