'''
Requirement:
Simulate a user login process
'''

# PREPARE DATA BEGIN -------------------------

database = [
    ['albert', '1234'],
    ['dilbert', '4242'],
    ['smith', '7524'],
    ['jones', '9843']
]

username = input("Username: ")
pin = input("Password: ")

# MAIN PROGRAM BEGINS ----------------------
if [username, pin] in database:
    print("Access granted.")
else:
    print("Wrong user/pass combination")