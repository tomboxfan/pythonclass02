'''
Requirement:
1) Ask user to input number from console
2) Add the number to the list in the correct order, so that the numbers are sorted asscendingly
3) Print list to the console
4) Exit the program when user input 'exit'
'''

# PREPARE DATA BEGIN ---------------------

# step 1) I define a list variable my_list, this is to hold all numbers from user
my_list = []

# Step 2) I need to define a str variable new_number_str, this is to store the number input from console by user
new_number_str = input("Next number: ")


# MAIN PROGRAM BEGIN ---------------------

# Step 3) I loop until new_number_str is 'exit'
while 'exit' != new_number_str:

    # Step 3.1) I conver the str new_number_str to int variable new_number
    new_number = int(new_number_str)

    # New Step)
    # I blindly append new_number to the end of my_list
    # Then I simply sort my_list
    my_list.append(new_number)
    my_list.sort()
    print(my_list)


    # Step 3.5) Update loop condition: Read next number from user
    new_number_str = input("Next number: ")
