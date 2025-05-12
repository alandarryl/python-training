# # mini project 1 : simple calculator
# # ask for operator

# operator = input("Enter operator (+, -, *, /): ")

# # ask for two numbers

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# # perform calculation

# if operator == '+':
#     result = num1 + num2
# elif operator == '-':
#     result = num1 - num2
# elif operator == '*':
#     result = num1 * num2
# elif operator == '/':
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         result = "Error! Division by zero."
# else:
#     result = "Invalid operator"
# # print result
# print("Result:", result)

# mini project 2 : simple calculator with functions

def calculate(operator, num1, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operator"
    
# ask for operator

operator = input("Enter operator (+, -, *, /): ")
# ask for two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# perform calculation
result = calculate(operator, num1, num2)
# print result

print("Result:", result)

# mini project 3 : simple calculator with functions and while loop

def calculate(operator, num1, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operator"
# ask for operator
while True:
    operator = input("Enter operator (+, -, *, /) or 'q' to quit: ")
    if operator == 'q':
        break
    # ask for two numbers
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    # perform calculation
    result = calculate(operator, num1, num2)
    # print result
    print("Result:", result)
    
# mini project 4 : simple calculator with functions and while loop and error handling

def calculate(operator, num1, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operator"
    
# ask for operator

while True:
    operator = input("Enter operator (+, -, *, /) or 'q' to quit: ")
    if operator == 'q':
        break
    # ask for two numbers
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue
    # perform calculation
    result = calculate(operator, num1, num2)
    # print result
    print("Result:", result)
   