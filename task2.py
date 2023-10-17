#TASK 2

#Design a simple calculator with basic arithmetic operations. Prompt the user to input two numbers and an operation choice. Perform the calculation and display the result.

def addition(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    if y ==0:
        print("denominator is Zero, Error")
    return x / y

def calculator():
    print("CALCULATOR")
    print("Operations That You can perform: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. multiplication")
    print("4. Division")

    choices = int(input("Enter the operation number you want to perform: "))
    if choices not in[1, 2, 3, 4]:
        print("Wrong input")
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    if choices ==1:
        result = addition(number1, number2)
        operator ="+"
    elif choices ==2:
        result = subtraction(number1, number2)
        operator ="-"
    elif choices ==3:
        result = multiplication(number1, number2)
        operator ="*"
    elif choices ==4:
        result = division(number1, number2)
        operator ="/"
    print(f"{number1} {operator} {number2} = {result}")


calculator()