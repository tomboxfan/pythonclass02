
x = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
print(x) # ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']

# Requirement 1: print a g j
# Requirement 2: print ['bb', ['ccc', 'ddd'], 'ee', 'ff']
# Requirement 3: print 'bb'
# Requirement 4: print ['ccc', 'ddd']
# Requirement 5: print 'ddd'
# Requirement 6: print 'ee'
# Requirement 7: print 'ff'



















































# Answer ----------------------------
# print(x[0], x[2], x[4])
# print(x[1])
# print(x[1][0])
# print(x[1][1])
# print(x[1][1][-1])
# print(x[1][1][1])
# print(x[1][2])
# print(x[1][3])
