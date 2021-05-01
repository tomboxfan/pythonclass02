import random

user_a_choice = input("User A's choice (scissors / paper / stone / exit): ")

while user_a_choice != 'exit':

    # CODE DELETE BEGIN -----------------
    # user_b_choice = input("User B's choice (scissors / paper / stone): ")
    # CODE DELETE END -----------------

    # CODE ADD BEGIN ---------------
    robot_choice = random.randint(1, 3)
    if robot_choice == 1:
        user_b_choice = 'scissors'
    elif robot_choice == 2:
        user_b_choice = 'paper'
    else:
        user_b_choice = 'stone'
    # CODE ADD END -----------------


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