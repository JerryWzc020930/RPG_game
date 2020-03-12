# The Main RPG-Game File
# Zicheng Wang (Jerry)
# Computer Science 30
# Period 4
# Date: 2020-3-10


"""Print descriptions of characters"""
characters = {"Rick Grimes": {"strength, damage of pistol +10", "health +10"},
              "Daryl Dixion": "precision, damage of crossbow +10",
              "Michonne": "speed, damage of machete +10",
              "Glenn Rhee": "firepower, damege of shotgun +10"
              }
# print the characters and their features
for character in characters:
    feature = characters[character]
    # Rick Grimes needs a nested loop because he has more than 1 feature
    if character == "Rick Grimes":
        RG = characters["Rick Grimes"]
        print(f"\n{character}'s feature:")
        for i in RG:
            print(f" -{i}")
    else:
        print(f"{character}'s feature:")
        print(f" -{feature}")


"""Print descriptions of locations in the game"""
locations = {"Hospital": "where the character wakes up",
             "Police station": "where the character gets weapons",
             "Pharmacy": "where the character gets medicines",
             "Survivors' camp": "where the character gets information"}
# Print out all the locations and descriptions
print("\n")
for location in locations:
    description = locations[location]
    print(f"{location} is {description}")


"""Print damage of weapons"""
weapons = {"machete": 60,
           "pistol": {"head": 90, "body": 60},
           "crossbow": {"head": 150, "body": 50},
           "shotgun": {"head": 200, "body": 120},
           "rifle": {"head": 150, "body": 90}}
# Print all the weapons and their damage
print("\n")
for weapon in weapons:
    if weapon == "machete":
        damage = weapons[weapon]
        print(f"The damage of {weapon} is {damage}")
    else:
        print(f"The damage of {weapon} is:")
        print(f"- {weapons[weapon]['head']} if you shoot head")
        print(f"- {weapons[weapon]['body']} if you shoot body")
# Weapons except machete are nested since they have 2 kinds of damage
