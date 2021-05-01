
# By default, print() insert a space between the items it prints.
print(1,2,3)
print(1,2,3, sep='-')
print(1,2,3, sep=' * ')
print(1,2,3, sep='\n') # this is next line

print('-' * 20)


# By default, print() adds a \n at the end of what it prints.
# You can change this by using the end parameter.
for i in range(5):
    print(i)

print('-' * 20)

for i in range(5):
    print(i, end = ' ')
