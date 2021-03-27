# Requirement: implement a calculator which supports + - * / ** between 2 numbers.

float_a = float(input("Number a: "))
float_b = float(input("Number b: "))
operator = input("Operator: ")
result = 0

if operator == '+':
    result = float_a + float_b
elif operator == '-':
    result = float_a - float_b
elif operator == '*':
    result = float_a * float_b
elif operator == '/':
    result = float_a / float_b
elif operator == '**':
    result = float_a ** float_b
else:
    print(f"Unrecognized operator {operator}")

print(f"{float_a} {operator} {float_b} = {result:.2f}")