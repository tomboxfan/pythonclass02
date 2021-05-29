fruits = ["Apple", 'Orange', "Banana", 'Pear']
animals = ['tiger', 'elephant', 'snake', 'shark']

#Solution 1: Use append - add new value to the END of the list
fruits.append("Whatermelon")
print(fruits)


# List can be heterogeneous (list can contain all kinds of values)
fruits.append(True)       # add a boolean value to the end of the list
fruits.append(1)          # add a int value to the end of the list
fruits.append(1.2)        # add a float value to the end of the list
fruits.append([1,2,3])    # add another list to the end of the list
print(fruits)

'''
       ['tiger', 'elephant', 'snake', 'shark']
index     0          1          2        3
         -4         -3         -2       -1

'''


# Solution 2: Use insert - add new value to the list at index specified
animals.insert(1, 'leopard')
print(animals) # ['tiger', 'leopard', 'elephant', 'snake', 'shark']
animals.insert(100, "giraffe") # when the indexs > length of the list, append it to the end of the list
print(animals) # ['tiger', 'leopard', 'elephant', 'snake', 'shark', 'giraffe']
animals.insert(-2, 'hedgehog')
print(animals) # ['tiger', 'leopard', 'elephant', 'snake', 'hedgehog', 'shark', 'giraffe']


# Solution 3: Use extend - join another list
insects = ['catepillar', 'ant', 'bufferfly']
animals.extend(insects)
print(animals)    # ['tiger', 'leopard', 'elephant', 'snake', 'hedgehog', 'shark', 'giraffe', 'catepillar', 'ant', 'bufferfly']

# animals.append(insects)
# print(animals) # ['tiger', 'leopard', 'elephant', 'snake', 'hedgehog', 'shark', 'giraffe', ['catepillar', 'ant', 'bufferfly']]



# Solution 4: Use + to join another list
birds = ['swallow', 'eagle', 'toucan']
# animals = animals + birds
animals += birds
print(animals) # ['tiger', 'leopard', 'elephant', 'snake', 'hedgehog', 'shark', 'giraffe', 'catepillar', 'ant', 'bufferfly', 'swallow', 'eagle', 'toucan']


# Solution 5: Use * to duplicate list
many_birds = birds * 3
print(many_birds) # ['swallow', 'eagle', 'toucan', 'swallow', 'eagle', 'toucan', 'swallow', 'eagle', 'toucan']

# Initialize the zero-valued list with 20 length
zeros_list = [0] * 20
print(zeros_list)