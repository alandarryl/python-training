def addition(first, second):
    result = first + second
    return result

def sub(first, second):
    result = first - second
    return result

def division(first, second):
    result = first / second
    return result

def multiplication(first, second):
    result = first * second
    return result

def power(first, second):
    result = first ** second
    return result

def modulo(first, second):
    result = first % second
    return result

def take_input():
    while True:
        try:
            first = int(input("first number : "))
            second = int(input("second number : "))
            numbers = [first, second]
        except ValueError:
            print("Your entry are invalid")
    return  numbers

working = True 

while working:
    print('''
        welcome in the menu make your choice : 
        1 - make a calculation 
        2 - see help
        3 - quit
        ''')
    entry = int(input("Enter an input : "))
    if entry == 3:
        working = False
    elif entry == 2:
        print("This program is a calculator, you can make different calcutation")
    elif entry == 1:
        calcul = True
        while calcul:
            print('''
                Select the calcule you want to make :
                A - addition
                S - substraction
                D - division
                M - mutlitiplication
                Mo - modulo
                P - power 
                R - to return to the menu precedent
                ''')
            entry_second = input("Enter your choice : ")
            entry_second = entry_second.upper()
            if entry_second == "R":
                calcul = False
            elif entry_second == "A":
                numbers = take_input()
                result = addition(numbers[0], numbers[1])
                print(f"the result of your addition is : {result}")
            elif entry_second == "S":
                numbers = take_input()
                result = sub(numbers[0], numbers[1])
                print(f"the result of your substraction is : {result}")
            elif entry_second == "D":
                numbers = take_input()
                try:
                    result = division(numbers[0], numbers[1])
                    print(f"the result of the division is : {result}")
                except ZeroDivisionError:
                    print("there is an error you should not try to divide the first number by zero")
            elif entry_second == "M":
                numbers = take_input()
                result = multiplication(numbers[0], numbers[1])
                print(f"the result of the multiplication is : {result}")

