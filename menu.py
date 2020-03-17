# Zicheng Wang (Jerry)
# Computer Science 30
# Period 4
# 2020-03-17
# a simple menu of actions


"""Action menu"""
# Possible actions
actions = ["load", "shoot", "open the door", "lock the door"]
# Print intro to the room
print("\nYou wake up in a hospital room and see a door in front of you.")
print("You find the key to the door, a pistol and ten bullets in your pocket.")
print("Here are something you can do:")
for action in actions:
    print(f"-{action}")
# Ask for input
message1 = input("\nWhat do you want to do: ")
if message1 == "load":
    print("\nYour pistol is now loaded.")
elif message1 == "shoot":
    print("\nBe careful, the sound of gunfire will draw zombies' attention.")
elif message1 == "open the door":
    print("\nYou open the door and see 10 zombies standing in the lobby.")
elif message1 == "lock the door":
    print("\nYou lock the door. Zombies won't break in for now.")
else:
    print("\nInvalid action.")


"""Direction menu"""
# Print possible directions
directions = ["east", "west", "north", "south"]
print("\nIf you want to explore the room,")
print("here are some directions you can go:")
for direction in directions:
    print(f"-{direction}")
# Ask for input
message2 = input("\nWhere do you want to go: ")
if message2 == "east":
    print("\nYou go east and find a box of bullets.")
    print("bullets + 10")
elif message2 == "west":
    print("\nYou go west and find a pocket knife in a closet")
elif message2 == "north":
    print("\nYou go north and find a window.")
    print("You open the window and see an SUV parked outside.")
elif message2 == "south":
    print("\nYou go south and find a dead end.")
else:
    print("\nInvalid direction")
