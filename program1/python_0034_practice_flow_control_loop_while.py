'''
Requirement: Print all numbers smaller than 7, odd or even.
'''

a = 1
while a < 7:
    if a % 2 == 0:
        print(a, 'is even.')
    else:
        print(a, 'is odd.')
    a+=1 # last step is to update the loop condition