from mymath import add
from mymath import sub as s

operation = input("Choose  an operation (add/sub): ").strip().lower()
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if operation == "add":
    result = add(a, b)
elif operation == "sub":
    result = s(a, b)
else:
    print("Invalid operation")
    exit()

print("Result =", result)
