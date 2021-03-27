# There are 3 boolean operators in Python: and / or / not
# there are 2 values in bool type: True / False

print("'and' rule -------------------")
print(f"'True and True' is {True and True}")
print(f"'True and False' is {True and False}")
print(f"'False and True' is {False and True}")
print(f"'False and False' is {False and False}")

print("'or' rule -------------------")
print(f"'True or True' is {True or True}")
print(f"'True or False' is {True or False}")
print(f"'False or True' is {False or True}")
print(f"'False or False' is {False or False}")

print("'not' rule -------------------")
print(f"'not True' is {not True}")
print(f"'not False' is {not False}")

bool_a = True
bool_b = False
bool_c = True
bool_d = False

print("-- Let's do some practice ----------------")
print(bool_a and bool_b and bool_c and bool_d) # False
print(bool_a or bool_b or bool_c or bool_d) # True


# or - lowest priority, so it equals to
# bool_a and bool_b                or                    bool_c and bool_d
print(bool_a and bool_b or bool_c and bool_d) # False

# bool_a   and   (bool_b or bool_c)    and     bool_d
print(bool_a and (bool_b or bool_c) and bool_d)  # False


# not - highest priority, it equals to
# bool_a     and      not bool_b      and      bool_c       and       not bool_d
print(bool_a and not bool_b and bool_c and not bool_d)  # True