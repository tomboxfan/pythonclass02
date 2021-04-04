'''
Requirement:
Ask user to input 3 numbers from console, sort the 3 numbers asscendingly.
'''

x = int(input("Please input x: "))
y = int(input("Please input y: "))
z = int(input("Please input z: "))

print(x, y, z)

if x <= y <= z:
    print(x, y, z)

elif x <= z <= y:
    print(x, z, y)

elif y <= z <= x:
    print(y, z, x)

elif y <= x <= z:
    print(y, x, z)

elif z <= x <= y:
    print(z, x, y)

elif z <= y <= x:
    print(z, y, x)
