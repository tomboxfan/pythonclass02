'''
Requirement:
Find all the possible value for number X which satisfies the following condition:
1) X + 100 is a square number.
2) X + 100 + 168 is another square number.

X is in range [-100, 2000]
HINT: We introduce an algorithm to check whether a number is a square number in program 0022.
'''

'''
Logic first, Code second:
1) The range in [-100, 2000], so all I need is to loop all numbers from [-100, 2000]
2) For each number in the range, I just need to check whether the number X
    Whether X + 100 is a square number or not?
    Whether X + 100 + 168 is a square number or not? 
    If both are true, X is what I am looking for
'''

import math


for x_candidate in range(-100, 2001):

    sqr_num_1 = x_candidate + 100
    sqr_num_2 = sqr_num_1 + 168

    sqr_root_for_sqr_num_1 = math.sqrt(sqr_num_1)
    sqr_root_for_sqr_num_1_int = int(sqr_root_for_sqr_num_1)

    if sqr_root_for_sqr_num_1 != sqr_root_for_sqr_num_1_int:
        continue # sqr_num_1 is not a square number, no need to check further. Let's check the next x_candidate.

    sqr_root_for_sqr_num_2 = math.sqrt(sqr_num_2)
    sqr_root_for_sqr_num_2_int = int(sqr_root_for_sqr_num_2)

    if sqr_root_for_sqr_num_2 != sqr_root_for_sqr_num_2_int:
        continue # sqr_num_2 is not a square number, no need to check further. Let's check the next x_candidate.

    print(x_candidate, "is such a number.")


