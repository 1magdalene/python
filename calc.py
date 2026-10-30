#A simple arithmetic calculator
def add(x, y):
    return round(x + y, 2)

def subtract(x, y):
    return round (x - y, 2)

def multiply(x, y):
    return round (x * y, 2)

def divide(x, y):
    return round(x / y, 2)

operator = input("What operator would you like to use? ")

if operator == "+":
    x = float(input("What is the first number? "))
    y = float(input("What is the second number? "))
    print(f"{x} + {y} = {add(x, y)}")
elif operator == "-":
    x = float(input("What is the second number? "))
    y = float(input("What is the first number? "))
    print(f"{x} - {y} = {subtract(x,y)}")
elif operator == "*":
    x = float(input("What is the first number? "))
    y = float(input("What is the second number? "))
    print(f"{x} * {y} = {multiply(x,y)}")
elif operator == "/":
    x = float(input("What is the first number? "))
    y = float(input("What is the second number? "))
    print(f"{x} / {y} = {divide(x, y)}")
else:
    print("Invalid operator")
