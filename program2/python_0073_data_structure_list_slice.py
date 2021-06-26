
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

print("6) Slice at Beginning & End ----------------------------")
print(L[:3]) #
# L[:3] doesn't have step, so python assumes step equals to 1
# When step equals to 1, when start is missing, Python assumes slice start from the left beginning.
# L[:3] equals to L[0:3]

print(L[6:]) #
# L[6:] doesn't have step, so python assumes step equals to 1
# When step equals to 1, when stop is missing, Python assumes slice end till the right end.
# L[6:] equals to L[6:len(L)]

print("7) Reverse a list ----------------------------")
print(L[::-1]) #
# step equals to -1, meaning the direction is from right to left.
# start is missing, stop is missing.
# So python will start from the right end, to the left beginning.

print("8) Modify multiple list values ----------------")
L = list("abcde")

# positive index:    0    1    2    3    4
#                  ['a', 'b', 'c', 'd', 'e']
# negative index:   -5   -4   -3   -2   -1

L[1:4] = [1, 2, 3]
print(L) #

L = list("abcde")
L[1:2] = [1, 2, 3]
print(L) #

print("9) Insert multiple list items -----------------")
L = list("abc")

# positive index:    0    1    2
#                  ['a', 'b', 'c']
# negative index:   -3   -2   -1

L[:0] = [1,2,3]
print(L) #
# L[:0] doesn't have step, so Python assumes step equals to 1
# When step equals to 1, meaning the direction is from left to right.
# start is missing, Python assumes slice start from the left beginning.
# L[:0] equals to L[0:0]
# When start equals to stop, it points to a position
# So when you assign a list to a position of L, you actually insert list [1, 2, 3] into list L at position 0

L = list('abc')
L[len(L):] = [1,2,3]
# L[len(L):] doesn't have step, so Python assumes step equals to 1
# When step equals to 1, meaning the direction is from left to right.
# stop is missing, Python assumes slice stop till the right end.
# L[len(L):] equals to L[len(L):len(L)] (L[3:3]
# When start equals to stop, it points to a position
# So when you assign a list to a position of L, you actually insert list [1, 2, 3] into list L at position 3
print(L)  #


print("10) Delete multiple list items -----------------")
L = list("abcde")

# positive index:    0    1    2    3    4
#                  ['a', 'b', 'c', 'd', 'e']
# negative index:   -5   -4   -3   -2   -1

L[1:5] = []
print(L) #

L = list("abcde")
del L[1:5]
print(L) #


print("11) Clone or Copy a list ------------------------")
L1 = list("abcde")
print(L1) #
L2 = L1[:]
print(L2) #
print(L2 is L1) # False

L3 = L1
print(L3) #
print(L3 is L1) # True

L1.append('f')
print(L1) #
print(L2) #
print(L3) # 





