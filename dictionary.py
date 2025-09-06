

# customer = {
#     "name" : "John",
#     "number" : 123,
#     "mail" : "jhon@gmail.com",
#     "is_verify" : True
# }

# customer["name"] = "jack"

# print(customer.get("name"))

# phone = input("Phone: ")

# digits_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four"
# }
# output = ""
# for ch in phone:
#     output += digits_mapping.get(ch, "!") + " "
# print(output)

# message = input("> ")
# words = message.split(' ')
# emojis = {
#     "happy" : ":)",
#     "sad" : ":("
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word)+ " "
# print(output)

# name = input("enter your name: ")
# def greet_user(n):
#     print("hi " + n + ", glad to see you")


# greet_user(name)


# def calc_cost (total, shipping, discount):
#     sum = total + shipping + discount
#     return sum


# value = calc_cost(80, 14, discount=0.5)

# print(value)

# def square(number):
#     number = int(number)
#     return number * number

# user = input(' Enter a number: ')

# result = square(int(user))

# print(f" the square of your number is {result}")



# def get_input(message):


# user = input(" Enter your message with space please: ")

# process (get_input(user))

# try:
#     def emoji_converter(message):
#         words = message.split(" ")

#         emojis = {
#             "happy": ":)",
#             "sad": ":(",
#             "flirt": ";)"
#         }
#         output = ""
#         for word in words:
#             output += emojis.get(word, word) + " "
#         return output


#     message = input("> ")
#     result = emoji_converter(message)

#     print(result)

# except ValueError:
#     print('You enter and invalid value')


try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("Invalid entry")





