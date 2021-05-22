'''
What is data structure?
Variable is like a pointer, it points to a box, which holds a value - int / float / boolean / str
Data structure is like a cabinet, which contains many boxes!
When the variable pointer, points to a cabinet, then you can use the variable to open the cabinet, and use any value inside the cabinet.

The first day structure we learn today is called - list

List: Python's workhorse
'''

# Solution 1: Use square bracket
fruits = ['Apple', 'Orange', 'Banana', 'Pear']
print(fruits)

animals = [ 'tiger',
            'elephant',
            'snake',
            'shark' ]

print(animals)

cars = [] # create an empty list
print(cars)

# Solution 2: Use list constructor
students = list() # Create an empty list
print(students)

numbers = list(range(1, 1000, 5)) # Pass in a range value to create numbers list
print(numbers)

char_list = list("I love Python!") # Pass in a str value to create char list
print(char_list)