# RPG game
# Zicheng Wang (Jerry)
# Computer Science 30
# Period: 4
# Date created: 2020-03-04
# Description: some basic RPG game commands using learned algorithm

"""original"""
# Original weapon list
weapons = ['pistol', 'sword', 'crossbow']
# Original medicine list
meds = ['energy_drink', 'painkiller', 'first_aid_kit', 'bandage']
print("\nThis is the original weapon list:")
for weapon in weapons:
    print(weapon)
print("This is the original medicine list:")
for med in meds:
    print(med)


"""adding new items"""
weapons.append('rifle')  # Add rifle to the weapon list
weapons.insert(0, 'pocket_knife')  # Add pocket_knife to the weapon list
# Print the updated weapon list
print("\nYou opened a treasure chest and find 2 new weapons")
print(f"This is your updated weapon list {weapons}")


"""deleting items"""
popped_weapons = weapons.pop()  # Delete rifle from the weapon list
print(f"\nYou just broke your {popped_weapons}")
print(f"You still have {weapons} left")  # Print the updated weapon list
meds.remove('bandage')  # Remove bandage from the medicine list
del meds[2]  # Delete first-aid-kit from the meds list
print("\nYou just used all of your bandage")
print("You just used your First Aid Kit")
print(f"You still have {meds} left")  # Print the updated medicine list


"""sorting items"""
meds.append('epinephrine')  # Add epinephrine to the meds list
meds.append('bandage')  # Add bandage to the meds list
print("\nYou just found 2 new medicines")
print(f"This is your medication list in alphabetical order {sorted(meds)}")
# Show that the order of the original list is not changed
print(f"In orginal order{meds}")
meds.sort()  # Change the list to alphabetical order
print(f"In alphabetical order {meds}")
meds.reverse()  # Change the list to reverse alphabetical order
print(f"In reverse alphabetical order {meds}")


"""finding length"""
# Print the length of the weapon list
print(f"\nYou have {len(weapons)} weapons")
# Print the length of the medicine list
print(f"You have {len(meds)} medicines")
