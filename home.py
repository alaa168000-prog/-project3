num1 =float(input("enter first number"))
operator =input("enter operator")
num2 =float(input("enter second number"))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "**":
    print(num1 ** num2)
else:
    print("invalid operator")

if num1 > num2:
    print(num1, "is greater than", num2)
elif num1 < num2:
    print(num1, "is less than", num2)
else:
    print(num1, "is equal to", num2)

if num1 > 0:
    print(num1, "is positive")
elif num1 < 0:
    print(num1, "is negative")
else:
    print(num1, "is zero")