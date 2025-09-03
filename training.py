

# character movement code prototype

score = 0
name = input("Enter your character's name: ")
print(f'Welcome {name}!')

print(f'{name} this is a simple text-based adventure game.')

print('Your mission is to navigate through the game and beat the final boss.')

game_runing = True

while game_runing:
    print('you arrive in a dark forest and have multiple options what will you do ? ')
    print("will you go left (L), right(R) or forward (F) ?")
    command = input(" > ").lower()
    if command == 'l':
        print('you meet a goblin what will you do ?')
        print('will you fight (F) or run (R) ?')
        command = input(' > ').lower()
        if command == 'f':
            print('you defeated the goblin!')
            score += 1
            print(f'your score is {score}')
        elif command == 'r':
            print('you ran away safely')
        else:
            print('invalid command')
            

    

