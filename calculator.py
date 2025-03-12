num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

operator = input("Enter an operator: ")

if operator == "+":
    res = float(num1) + float(num2)
    print(res)
elif operator == "-":
    res = float(num1) - float(num2)
    print(res)
elif operator == "*":
    res = float(num1) * float(num2)
    print(res)
elif operator == "/":
    res = float(num1) / float(num2)
    print(res)
else:
    print("Invalid operator")