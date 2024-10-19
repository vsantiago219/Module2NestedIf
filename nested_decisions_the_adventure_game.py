#Task 1 - Buggy Code

place = input("Choose a place: (forest, cave) \n")

if place == "forest": 
    action = input("Choose an action: (climb a tree, cross a river) \n")

    if action == "climb a tree":
        print("You found a bird's nest!")
    if action == "cross a river":
        print("You found a boat!")
if place =="cave":
    print("You find a hidden treasure!")

#Task 2 - Setting the Scene

place = input("Choose a place: (forest, cave) \n")

if place == "forest": 
    action = input("Choose an action: (climb a tree, cross a river) \n")

    if action == "climb a tree":
        print("You found a bird's nest!")
    if action == "cross a river":
        print("You found a boat!")
if place =="cave":
    print("How would you like to proceed?")
    light = input("Choose a light source: (torch, dark) \n")
    if light == "torch":
        print("The torch will light your path")
    else:
        print("Use caution as you proceed")

#Task 3 - Default Path

place = input("Choose a place: (forest, cave) \n")

if place == "forest": 
    action = input("Choose an action: (climb a tree, cross a river) \n")

    if action == "climb a tree":
        print("You found a bird's nest!")
    if action == "cross a river":
        print("You found a boat!")
if place =="cave":
    print("You find a hidden treasure!")
else:
    pass

place = input("Choose a place: (forest, cave) \n")

if place == "forest": 
    action = input("Choose an action: (climb a tree, cross a river) \n")

    if action == "climb a tree":
        print("You found a bird's nest!")
    if action == "cross a river":
        print("You found a boat!")
if place =="cave":
    print("How would you like to proceed?")
    light = input("Choose a light source: (torch, dark) \n")
    if light == "torch":
        print("The torch will light your path")
    if light == "dark":
        print("Use caution as you proceed")
    else:
        pass