import random

computer_option = ["r", "p", "s"]

game_logic ={
    "r" : "s",
    "p" : "r",
    "s" : "p"
}

working = True

computer_score = 0
player_score = 0
number_play = 0

while working:
    print('you are playing rock paper scissor against the computer')
    choice = input("enter your choice (R, P, S) > ").lower()
    if choice not in computer_option:
        print("your choice is invalid!")
        continue
    computer_choice = random.choice(computer_option)
    if choice == computer_choice:
        print("you are tie")
        number_play +=1
    elif game_logic[choice] == computer_choice:
        print("congrats you win!")
        player_score +=1
        number_play +=1
    else:
        print('You lose !')
        computer_score += 1
        number_play +=1
    if number_play == 5:
        print("you have played five time the game end here")
        working = False

print(f" the computer score : {computer_score}, the player scored {player_score}")







