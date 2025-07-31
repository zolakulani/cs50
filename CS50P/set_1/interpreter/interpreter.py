num1, operator, num2 = input("Expression: ").split()
num1 = int(num1)
num2 = int(num2)

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2    
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operator"

print(f"{result:.1f}")