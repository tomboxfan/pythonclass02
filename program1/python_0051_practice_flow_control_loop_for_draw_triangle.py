'''
Right triangle 1
1st line: 1 '*'
2nd line: 2 '*'
...
10th line: 10 '*'

Summary:
loop 0 - 9: print 1,2,3...10 '*'
'''

for line_number in range(10):
    print('*' * (line_number + 1))

print('\n\n---------------------------------------\n\n')

'''
Right triangle 2
1st line: 9 ' ' + 1 '*'
2nd line: 8 ' ' + 2 '*'
...
10th line: 0 ' ' + 10 '*'

Summary:
loop 0 - 9: print 9,8,7...0 ' ', then I print 1,2,3,...10 '*'
'''
for line_number in range(10):
    print(' ' * (9 - line_number) + '*' * (line_number + 1))


print('\n\n---------------------------------------\n\n')

'''
hourglass
19 lines in total
read from the 1st line:
1st line: 0 ' ' + 19 '*'
2nd line: 1 ' ' + 17 '*'
...
9th line: 8 ' ' + 3 '*'
10th line: 9 ' ' + 1 '*'
11th line: 8 ' ' + 3 '*'
...
19th line: 0 ' ' + 19 '*'

Because it is symmetrical, so I loop in range(-9, 10)
loop: -9 to 9: print 0,1,2...8,9,8...1,0 ' '; then print 19,17,15,....3,1,3...15,17,19 '*'
'''
for line_number in range(-9, 10):
    print(' ' * (9 - abs(line_number)) + '*' * (abs(line_number) * 2 + 1))

