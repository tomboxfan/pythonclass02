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
isosceles triangle
1st line: 9 ' ' + 1 '*'
2st line: 8 ' ' + 3 '*'
3st line: 7 ' ' + 5 '*'
...
10th line: 0 ' ' + 19 '*'

Summary:
Loop 0 - 9: print 9, 8, 7...0 ' '; then print 1, 3, 5, ... 19 '*'

'''

for line_number in range(10):
    print(' ' * (9 - line_number) + '*' * (line_number * 2 + 1))

print('\n\n---------------------------------------\n\n')

'''
parallelogram 

Summary:
Loop 0 - 9: print 9, 8, 7...0 ' '; then print 10 '*'
'''

for line_number in range(10):
    print(' ' * (9 - line_number) + '*' * 10)


print('\n\n---------------------------------------\n\n')

'''
obtuse triangle
1st line: 0 ' ' + 1 '*'
2nd line: 1 ' ' + 2 '*'
...
10th line: 9 ' ' + 10 '*'

Summary:
Loop from 0 - 9: print 0,1,2...9 ' '; then I print 1,2,3...10 '*'
'''

for line_number in range(10):
    print(' ' * line_number + '*' * (line_number + 1))

print('\n\n---------------------------------------\n\n')

'''
obtuse triangle 2
1st line: 18 ' ' + 1 '*'
2nd line: 16 ' ' + 2 '*'
...
10th line: 0 ' ' + 10 '*'

Summary:
Loop from 0 - 9: print 18, 16, 14, ... 0 ' '; then I print 1,2,3... 10 '*'

'''

for line_number in range(10):
    print(' ' * (18 - line_number * 2) + '*' * (line_number + 1))




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


print('\n\n---------------------------------------\n\n')

'''
triple isosceles triangle

we know how to print single isosceles triangle:


for line_number in range(10):
    print(' ' * (9 - line_number) + '*' * (line_number * 2 + 1))
    
but how to print triple isosceles triangle in 1 single for loop? 

single isosceles triangle loops in range(10), 10 numbers: 0 - 9    
triple isosceles triangle should loop in range(30), 10 numbers: 0 - 9, 10 - 19, 20 - 29

Question: How to make 10 -19 and 20 - 29 similar to 0 -9? 
Answer: Use % 10
'''

for line_number in range(30):
    print(' ' * (9 - line_number % 10) + '*' * (line_number % 10 * 2 + 1))

print('\n\n---------------------------------------\n\n')

'''
rhombus
19 lines in total
read from 1st line:
1st line: 9 ' ' + 1 '*'
2st line: 8 ' ' + 3 '*'
3st line: 7 ' ' + 5 '*'
...
10th line: 0 ' ' + 19 '*'
11th line: 1 ' ' + 17 '*'
...
19th line: 9 ' ' + 1 '*'

Summary:
Because it is symmetrical, so I need to loop in range(-9, 10) 

We learnt abs() function which can convert -9 - -1 to 9 to 1
'''

for line_number in range(-9, 10):
    print(' ' * abs(line_number) + '*' * (19 - abs(line_number * 2)))
    