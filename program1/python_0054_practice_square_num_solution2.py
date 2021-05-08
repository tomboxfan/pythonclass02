'''
Logic first, Code second:
Solution 0053 starts from X. It checks whether x + 100 and x + 100 + 168 are square numbers.
Solution 0054 starts from square numbers. It checks whether any 2 square numbers have a difference of 168.

1) As the maximum number is 2000, so 2000 + 100 + 168 = 2268 which is less than 2500.
   So the 2 square number mentioned above are all less than 50.

2) So all I need to do is loop all the square numbers from 1 to 2500 (1^2 to 50^2)
   See any square number a, plus 168, is another square number.
   If yes, then a - 100 is what I am looking for.
'''

import math

for sqr_root in range(1, 51):
    sqr_num_1 = sqr_root ** 2
    sqr_num_2 = sqr_num_1 + 168

    sqr_root_for_sqr_num_2 = math.sqrt(sqr_num_2)
    sqr_root_for_sqr_num_2_int = int(sqr_root_for_sqr_num_2)

    if sqr_root_for_sqr_num_2 != sqr_root_for_sqr_num_2_int:
        continue # sqr_num_2 is not a square number, no need to check further. Let's check the next sqr_root.

    print(sqr_num_1 - 100, 'is such a number!')

