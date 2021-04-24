'''
Requirement:
Step 1) Ask player_a to input 'scissors', 'paper', 'stone', 'exit'.
Step 2) Use while loop, loop as long as player_a's input is NOT 'exit'.
Step 3) Inside the while loop body, you ask player_b to input 'scissors', 'paper', 'stone'.
Step 4) Use if / elif / else or nested if / elif / else to check who wins, print the result.
'''

'''
================
Thinking Logic
================


----------------------------------------------------
For all python programs, step 1) prepare 'data'
----------------------------------------------------

For this question, what is 'data'?
player_a's choice, being 'scissors' / 'paper' / 'stone' / 'exit', is data.
player_b's choice, being 'scissors' / 'paper' / 'stone', is data.

Step 1, player a's choice should be saved into a variable, 'user_a_choice'
Step 2, while user_a_choice != 'exit':
Step 3, player b's choice should be saved into a variable, 'user_b_choice'
Step 4, comparing user_a_choice vs user_b_choice, tell who wins.

    we use top-down coding solution, finish the skeleton first.
    
    if user_a_choice == 'scissors':
        pass # Place holder
    elif user_a_choice == 'paper':
        pass # Place holder
    elif user_a_choice == 'stone':
        pass # Place holder
    else:
        print(f"User A inputs a wrong choice: {user_a_choice} ")

    inside the 3 Place holder above, I can fill in this code:
    
    if user_b_choice == 'scissors':
        pass # Place holder
    elif user_b_choice == 'paper':
        pass # Place holder
    elif user_b_choice == 'stone':
        pass # Place holder
    else:
        print(f"User B inputs a wrong choice: {user_a_choice} ")
        
'''

user_a_choice = input("User A's choice (scissors / paper / stone / exit): ")

while user_a_choice != 'exit':

    user_b_choice = input("User B's choice (scissors / paper / stone): ")

    if user_a_choice == 'scissors':
        if user_b_choice == 'scissors':
            print(f"User A {user_a_choice}, User B {user_b_choice}: Draw.")
        elif user_b_choice == 'paper':
            print(f"User A {user_a_choice}, User B {user_b_choice}: User A wins.")
        elif user_b_choice == 'stone':
            print(f"User A {user_a_choice}, User B {user_b_choice}: User B wins.")
        else:
            print(f"User B inputs a wrong choice: {user_a_choice} ")

    elif user_a_choice == 'paper':
        if user_b_choice == 'scissors':
            print(f"User A {user_a_choice}, User B {user_b_choice}: User B wins.")
        elif user_b_choice == 'paper':
            print(f"User A {user_a_choice}, User B {user_b_choice}: Draw.")
        elif user_b_choice == 'stone':
            print(f"User A {user_a_choice}, User B {user_b_choice}: User A wins.")
        else:
            print(f"User B inputs a wrong choice: {user_a_choice} ")


    elif user_a_choice == 'stone':
        if user_b_choice == 'scissors':
            print(f"User A {user_a_choice}, User B {user_b_choice}: User A wins.")
        elif user_b_choice == 'paper':
            print(f"User A {user_a_choice}, User B {user_b_choice}: User B wins.")
        elif user_b_choice == 'stone':
            print(f"User A {user_a_choice}, User B {user_b_choice}: Draw.")
        else:
            print(f"User B inputs a wrong choice: {user_a_choice} ")

    else:
        print(f"User A inputs a wrong choice: {user_a_choice} ")

    # IMPORTANT !!! ---------------------------------
    # Update looping condition
    # -----------------------------------------------
    user_a_choice = input("User A's choice (scissors / paper / stone / exit): ")