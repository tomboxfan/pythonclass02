'''
This code is another solution to question 0052
'''

# PREPARE DATA BEGIN ===============================================

# Step 1) Define variable profit - I read annual profit from console
profit = int(input("total profit of the year: "))

# Step 2) Define variable bonus - use float constructor to create a float variable which equals to 0
bonus = float()

# Step 3) Define variable thresholds and rates which represent the table definition above
thresholds = [1000000, 1000000, 2000000, 2000000, 4000000]
rates = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]
# Attention! 5 numbers in thresholds, 6 numbers in rates!


# MAIN PROGRAM BEGIN ==============================================

for i in range(5):

    if profit <= thresholds[i]:
        bonus += profit * rates[i]

        # OLD CODE ------------------
        # print(f"We should keep ${bonus} to our staff for this outlet.")
        # exit()  # built-in function exit() will cause the program exit
        # ---------------------------

        # NEW CODE ------------------
        break
        # ---------------------------

    bonus += thresholds[i] * rates[i]
    profit -= thresholds[i]

else:
    bonus += profit * rates[5]  # tier 5 


print(f"We should keep ${bonus} to our staff for this outlet.")

