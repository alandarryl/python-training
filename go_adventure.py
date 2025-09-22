location = {
    "forest": "You are in a dark forest. Two roads lie ahead.",
    "village": "You arrive at a small, quiet village.",
    "tavern": "You step into the tavern. It smells of ale and adventure.",
    "shop": "You are in the shop. Items glimmer on the shelves.",
    "cave": "A dark cave looms before you.",
    "deepest_cave": "You reach the deepest part of the cave..."
}

route_option = {
    "forest": ["village", "cave"],
    "village": ["tavern", "shop", "forest"],
    "tavern": ["village"],
    "shop": ["village"],
    "cave": ["forest", "deepest_cave"],
    "deepest_cave": ["cave"]
}

def display_info(place):
    print(location[place])
    print("Your options are:")
    options = route_option[place]
    for i, opt in enumerate(options, 1):
        print(f"{i} - {opt}")




adventuring = True
place = "forest"

while adventuring:
    display_info(place)
    try:
        choice = int(input("> ")) - 1
        options = route_option[place]

        if 0 <= choice < len(options):
            place = options[choice]
        else:
            print("That’s not a valid option.")
    except ValueError:
        print("Please enter a number.")






