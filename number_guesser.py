import random

def user_entry():
    while True:
        try:
            guess = int(input("Enter a number : "))
            return guess
        except ValueError:
            print("please enter a number")

working = True
computer_number =random.randint(1, 10)
number_guesses = 0

while working:
    print("try to guess the computer number ")
    guesses = user_entry()
    if guesses == computer_number:
        print(f"You guess the right number : {guesses}")
        working = False
    elif guesses > computer_number:
        print("you number is too high")
        number_guesses += 1
    elif guesses < computer_number:
        print("your guesses is too low")
        number_guesses +=1
print(f"you try to guess {number_guesses}")


