
scores = [80, 90, 70, 60]

# ----------------------------
# Sort a list
# ----------------------------

# Solution 1) built-in function sorted()
sorted_scores = sorted(scores)
print(sorted_scores)        # [60, 70, 80, 90]
print(scores)               # [80, 90, 70, 60]

# Solution 2) method sort()
scores.sort()
print(scores)               # [60, 70, 80, 90]

# IMPORTANCE !!! -----------------------------------------------------
# built-in function: sorted(my_list)        create a NEW list with my_list's sorted values, my_list is NOT changed.
# my_list.sort()                            sort the values in my_list, my_list is changed
# --------------------------------------------------------------------

print("----------------------------------")

# ----------------------------
# Reverse a list
# ----------------------------

# Solution 1) built-in function sorted()
sorted_scores_reverse = sorted(scores, reverse=True)
print(sorted_scores_reverse)           #  [90, 80, 70, 60]
print(scores)                          #  [60, 70, 80, 90]

# Solution 2) method reverse()
scores.reverse()
print(scores)                          # [90, 80, 70, 60]

# IMPORTANCE !!! -----------------------------------------------------
# built-in function: sorted(my_list, reverse=True)        create a NEW list with my_list's sorted values, my_list is NOT changed.
# my_list.reverse()                                       reverse the values in my_list, my_list is changed
# --------------------------------------------------------------------