'''
Requirement:
You have 2 SORTED lists, merge the 2 lists into 1 new list. And this new list is SORTED as well.

merge
list_a = [1,5,7,9,13,15,24,27,78,110,167]
list_b = [2,2,6,8,16,17,18,19,99]
to list_ab

merge
list_c = [1,5,7]
list_d = [2,2,6,8,16,17,18,19,99]
to list_cd

merge
list_e = []
list_f = [2,2,6,8,16,17,18,19,99]
to list_ef
'''

'''
Logic / Algorithm:

Step 1) I create 2 pointers index_a and index_b, their initial value are 0, so that they point to the 1st element of list_a and list_b 
Step 2) I loop forever, as I can break out of the loop myself
Step 3) Inside the loop body, I compare the 2 values which index_a and index_b points to.
        I append the smaller value to to result list, and move the index_a or index_b to the next position. 
        There are 3 situations:
        
        Situation 1) list_a has reached the end, list_b has NOT reached the end.
        -> append the remaining values of list_b to new_list
           then break the loop
        
        Situation 2) list_a has NOT reached the end, list_b has reached the end.
        -> append the remaining values of list_a to new_list
           then break the loop
           
        Situation 3) list_a has NOT reached the end, list_b has NOT reached the end.
        -> I compare list_a[index_a] vs list_b[index_b]. I append the smaller value to my new_list and move the index to the next.

Question: How to tell whether list_a has reached the end?
Answer: if len(list_a) is 10, the list_a index value is from 0 - 9.
        So when index_a == len(list_a), then index_a becomes invalid, then index_a is at the end of the list_a
'''

# PREPARE DATA BEGIN ===============================================

# This is the 2 lists given by the question
list_a = [1,5,7,9,13,15,24,27,78,110,167]
list_b = [2,2,6,8,16,17,18,19,99]

# This is to hold our final result
new_list = []

# These 2 point to the 1st value of list_a and list_b
index_a = 0
index_b = 0


# MAIN PROGRAM BEGIN ==============================================

while True:

    # Situation 1) list_a has reached the end, list_b has NOT reached the end.
    if index_a == len(list_a) and index_b < len(list_b):
        # append the remaining values of list_b to new_list
        new_list.extend(list_b[index_b:])
        break



    # Situation 2) list_a has NOT reached the end, list_b has reached the end.


    # Situation 3) list_a has NOT reached the end, list_b has NOT reached the end.




print(new_list)