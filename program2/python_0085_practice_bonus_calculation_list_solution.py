'''
This code is another solution to question 0052
'''

'''
Logic:

There are several boundaries in the question description:
1) 10% of the 1st million profit
2) 7.5% of the 2nd million profit
3) 5% of 3rd and 4th million profit
4) 3% of 5th and 6th million profit
5) 1.5% of 7th, 8th, 9th and 10th million profit
6) 1% of the remaining profit

This description can be converted to the table below:

    ======================
    threshold       rate
    ======================
    above           1%
    ---------------------
    4 million       1.5%
    ---------------------
    2 million       3%
    ---------------------
    2 million       5%
 ^  ---------------------
 |  1 million       7.5%
 |  ---------------------
 |  1 million       10%
-------------------------------------------
As profit goes up, the percentage goes down for each tier.

In 0052 solution 1, we use if / elif to check each tier.
After we learnt list, we can use list directly to loop each tier.

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

'''
I need to check whether the profit exceeds the thresholds values.

[tier 1]
    
    if profit <= 1,000,000                  if profit <= thresholds[0]:
        bonus = profit * 0.1                    bonus = profit * rates[0]
        finish                                  finish
        
    if profit > 1,000,000                   if profit > thresholds[0]:
        bonus = 1,000,000 * 0.1                 bonus = thresholds[0] * rates[0]
        profit = profit - 1,000,000             profit -= thresholds[0]
        go to [tier 2]                          go to [tier 2]

        
[tier 2]
    
    if profit <= 1,000,000                  if profit <= thresholds[1]:
        bonus = bonus + profit * 0.075          bonus += profit * rates[1]
        finish                                  finish
    
    if profit > 1,000,000                   if profit > thresholds[1]:
        bonus = bonus + 1,000,000 * 0.075       bonus += thresholds[1] * rates[1]
        profit = profit - 1,000,000             profit -= thresholds[1]
        go to [tier 3]                          go to [tier 3]


[tier 3]
... ...

[tier 4]
... ...

[tier 5]
... ...

[tier 6]



'''