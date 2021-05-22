'''
Requirement:
There is a group of monkeys who eat a pile of peaches.
On Day 1, they eat half plus 1
On Day 2, they eat half plus 1 again
...
On Day 10, they notice there is only 1 peach left before they eat.

Question:
1) How many peaches in total in Day 1?
2) Print out from Day 1, how many peaches in total? How many peaches they eat? How many peaches are left. Till last day.

'''

'''
Core Logic:

day 10:
peach_total = 1

day 9:
peach_left = 1
peach_total = (peach_left + 1) * 2

day 8:
peach_left (day 8) = peach_total (day 9)
peach_total = (peach_left + 1) * 2

day 7:
peach_left (day 7) = peach_total (day 8) 
peach_total = (peach_left + 1) * 2

 
'''

# There is 1 peach left in day 10
peach_total = 1
print(f"On day 10, there is {peach_total} peach before they eat.")

for day in range(9, 0, -1):
    peach_left = peach_total
    peach_total = (peach_left + 1) * 2
    # print(f"On day {day}, there are {peach_total} peaches before they eat.")

print(f"On day 1, there are {peach_total} peaches before they eat.") # Question 1) is done!

print("-------------------------------------------")

# Question 2)

for day in range(1, 10):
    peach_eaten = peach_total // 2 + 1
    peach_left = peach_total - peach_eaten
    print(f"On day {day}, there are {peach_total} initially. They eat {peach_eaten} peaches, and there are {peach_left} peaches left.")

    # And now, peach_left becomes next day's peach_total
    # update peach_total, so that the for loop can proceed.
    peach_total = peach_left

print(f"On day 10, there is {peach_total} peach left.")
