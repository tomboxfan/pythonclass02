# Requirement: Mimic online game user login

# define a multi-line str variable as the welcome message
# A multi-line str variable is surrounded by a pair of triple quote
welcome_msg = '''
******************************
   Welcome to King of Glory
******************************
'''

print(welcome_msg)


user_name = input("User Name: ") # 'User Name: ' is to prompt user what to type in the console. As soon as user sees 'User Name: " in the console, user knows, he needs to type his username.
password = input("Password: ")

print(f"Welcome, {user_name}! You've successfully logged in the game. ")

total_coins = 0

short_of_coins_msg = f"Unfortunately, you have only {total_coins} coins in your account. Please top up your account."
print(short_of_coins_msg)

coin_topup_str = input("Total coins to top up: ") # str type
coins_topup = int(coin_topup_str)

total_coins += coins_topup

# print(f"Now you have coins: {total_coins}. You can continue to play the game.")

#--Challenging Question:
# if user tops up coins less than 500, then you tell user you still don't have enough coins.
# If user tops up coins greater than 500, tell user, you can continue to play.
# -------------------------------------------
# Keep this Question OPEN till next lesson.
# -------------------------------------------

coins_requirment = 500

if total_coins < coins_requirment:
    print(f"You still do not have enough coins, you need to top up extra {coins_requirment - total_coins} coins")
else:
    print(f"Now you have coins: {total_coins}. You can continue to play the game.")
