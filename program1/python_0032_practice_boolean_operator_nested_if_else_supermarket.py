'''
Requirment:
1) implement NTUC supermarket price calculator.

2) Each time, a customer can buy 1 product - beef / pork / tomato / apple / orange

3) beef / pork / tomato - total price calculated by weight
   beef - $20 / kg
   pork - $16 / kg
   tomato - $5 / kg

4) apple / orange - total price calculated by quantity
   apple - $5 for 5 apples; $1.6 each
   orange - $5 for 3 oranges; $2 each

5) implement a membership system, member will get 10% discount
   i) You need to ask customer, "Are you a member?"
   ii) customer can answer 'y', 'Y', 'yes', 'Yes'. All 4 answers mean he is a NTUC member.

6) implement a payment system, which supports Visa/Mastercard/NETS/Cash
   i) If user pays with Visa/Mastercard, you need to ask user to sign his name. (Use input() to get user's signature)
   ii) If user pays with NETS, you ned to ask user to input his card password. (Use input() to get user's password)
   iii) If user pays with Cash, you need to check whether you should give customer some change, whether he has paid enough money, etc.
'''

welcome_msg = '''
**************************************
    Welcome to NTUC Supermarket
**************************************
'''

print(welcome_msg)

product_prices = '''
---------------------------------
   beef - $20 / kg
   pork - $16 / kg
   tomato - $5 / kg
   apple - $5 for 5 apples; $1.6 each
   orange - $5 for 3 oranges; $2 each   
---------------------------------
'''

print(product_prices)


product_name = input("What product do you want to buy (beef / pork / tomato / apple / orange): ")

total_price = 0

if product_name == 'beef' or product_name == 'pork' or product_name == 'tomato':

    total_weight = float(input("Total weight(kg): "))

    if product_name == 'beef':
        unit_price = 20
    elif product_name == 'pork':
        unit_price = 16
    else:
        unit_price = 5

    total_price = unit_price * total_weight
    print(f"{product_name}: ${unit_price} * {total_weight} = ${total_price}")

elif product_name == 'apple' or product_name == 'orange':
    pass # HOMEWORK

else:
    print(f"Unrecognized product: {product_name}")


# membership --------------------------------------------------------
member_str = input("Are you a member? ")

if member_str == 'Y' or member_str == 'y' or member_str == 'Yes' or member_str == 'yes':
    total_price *= 0.9 # total_price = total_price * 0.9
    print(f"After discount, total price: ${total_price}")

# payment ----------------------------------------------------------
payment = input("Will you pay using Visa / Mastercard / NETS / Cash? ")

if payment == 'Visa' or payment == 'Mastercard':
    signature = input("PLease sign your name: ")
    print(f"Signature {signature} is well received.")
    print(f"${total_price} has been charged to your {payment} card.")
elif payment == 'NETS':
    password = input("Please input your NETS password:")
    print(f"${total_price} has been charged to your NETS card.")
elif payment == 'Cash':
    pass # HOMEWORK
else:
    print("Unsupported payment.")