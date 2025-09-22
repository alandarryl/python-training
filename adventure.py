

location = {
    "forest": "welcome in the dark forest, there is two road where do you want to go",
    "village": "welcome in our small village",
    "tavern": "welcome in the village tavern you can buy thing here",
    "shop": "welcome in the shop, you can buy new things here",
    "cave": "you enter a dark cave with an omnious air ",
    "deepest cave": "you reach the deepest of the cave"
}

route_option = {
    "forest":["left road", "right road", ""],
    "village": ["tavern", "shop", "cave"],
    "tavern":["ask for info", "save your progress", "quit the game"],
    "shop":["buy items", "sell items", "upgrade items"],
    "cave":["go deeper", "camp", "go back"],
    "deepest cave": ["fight boss", "leave", "give up"]
}

def display_info(place):
    print(f"{location[place]}")
    print(f"here are your oprtion")
    for i, option in enumerate(route_option[place], start=1):
        print(f"{i} - {option}")
        i +=1

adventuring = True
place = "forest"
print("You are a young man wondering alone ")

while adventuring:
    display_info(place)
    try:
        player_choice = input(" > ")
        if player_choice == "1":
            print("you took a wrong turn you find yourself in a dangerous situation and get kill")
            adventuring =False
        elif player_choice =="2":
            print("you follow the road through the forest and en up in a small village")
            place = "village"
            display_info(place)
    except ValueError:
        print("your option is wrong")
print("your adventure end here!")







