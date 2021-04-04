'''
Requirement:
Ask user to input 3 numbers from console, sort the 3 numbers asscendingly.
'''

x = int(input("Please input x: "))
y = int(input("Please input y: "))
z = int(input("Please input z: "))

print(x, y, z)

if x <= y and x <= z and y <= z:
    print(x, y, z)

elif x <= y and x <= z and y > z:
    print(x, z, y)

elif y <= x and y <= z and z <= x:
    print(y, z, x)

elif y <= x and y <= z and z > x:
    print(y, x, z)

elif z <= x and z <= y and x >= y:
    print(z, x, y)

elif z <= x and z <= y and x < y:
    print(z, y, x)
