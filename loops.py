

# isExisting = True

# while isExisting:
#     command = input(' type exit to exit the loop : ')
#     if command == 'exit':
#         isExisting = False
#         print('you are out of the loop')
#     else:
#         print('you are still in the loop')

# i = 1

# while i <= 5:
#     print('*'*i)
#     i += 1
# print('loop ended')

# guess_count = 0
# secret_number = 7
# guess_limit = 3

# while guess_count < guess_limit:
#     command = int(input('guess the secret number between 1 to 10 : '))
#     if command == secret_number:
#         print('you guess the right number')
#         break
#     else:
#         guess_count += 1
#         print(f'you have {guess_count} guess_count left')
#         if guess_count == 0:
#             print('you are out of guess_counts, game over')
#         else:
#             print('try again')

# running = True
# is_moving = False

# while running:
#     user_input = input('Enter a command (help to get see all command) > ')
#     command = user_input.lower()
#     if command == 'help':
#         print('''
#             start - to start the car
#             stop - to stop the car
#             quit- to exit the program
#             ''')
#     elif command == 'start':
#         if is_moving:
#             print('car is already moving!')
#         else:
#             print('car started... ready to go!')
#             is_moving = True
#     elif command == 'stop' and is_moving:
#         print('car stopped.')
#         is_moving = False
#     elif command == 'stop' and not is_moving:
#         print('car is already stopped!')
#     elif command == 'quit':
#         running = False
#     else:
#         print("i don't understand that...")
# else:
#     print('program ended')


# for item in range(0, 100, 2):
#     print(item)


# prices = [10, 20, 30]
# sum = 0

# for item in prices:
#     sum += item
# print(f"our total price is {sum}")


# for x in range(0, 10, 2):
#     for y in range(0, 10, 3):
#         if x == y:
#             print(f" cross coordinate ({x}, {y})")
#         elif x!= y:
#             print(f"different coordinate of {x}, {y}")

# numbers = [5, 2, 5, 2, 2]

# for x in range(0, 1):
#     for y in numbers:
#         print('X' * y)

# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += 'x'
#     print(output)