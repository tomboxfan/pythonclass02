
# IMPORTANCE !!! --------------------------------------
# Assume L is a list, expression L[start:stop:step] returns a portion of list L, starts from index start (inclusive), to index stop (exclusive), at a step size 'step'.
#
# Slice syntax:
#                  L[start:stop:step]
#
# start:  start position (inclusive)
# stop:   stop position (exclusive)
# step:   the increment
# -----------------------------------------------------

L = list('abcdefghi')
print(L)


# positive index:       0    1    2    3    4    5    6    7    8
#                     ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# negative index:      -9   -8   -7   -6   -5   -4   -3   -2   -1


print("1) Basic Example ------------------------------------------")
# L[2] is included. L[7] is excluded.
# This is the same as range(2,10) which generates number [2, 10). 2 is inclusive ( closed interval), 10 is exclusive (open interval)
print(L[2:7])
# start: 2
# stop: 7
# step: 1
# L[2:7] doesn't have step, so Python assumes step equals to 1.
# So L[2:7] equals to L[2:7:1]
print(L[2:7:1])

print("2) Slice with Negative Indices ---------------------------")
print(L[-7:-2])
# start: -7
# stop: -2
# step: 1
print(L[-7:-2:1])

print("3) Slice with Postive and Negative Indices --------------")
print(L[2:-5])

print("4) Specify step of the Slicing --------------------------")
print(L[2:7:2])   #

print("5) Negative Step Size -----------------------------------")
print(L[6:1:-1])  #
print(L[6:1:-2])  #