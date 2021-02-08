  
# Imports
import time, random

print("Welcome to Fjot Adventures!")
print("Choose a fjot:")
fjotChosen = input("Shidneka (extinct), Bghaydsa (new) ")
print("You have chosen",fjotChosen)
if fjotChosen == "Shidneka":
    print("You are the last of your kind. Try to survive.\n——  > ——\nO-----O\n==========\n/+++++++++|\n /+++++++|\nc c c c c c c c c")
elif fjotChosen == "Bghaydsa":
    print("You have many Fjot friends to support you in your journey.\n==========\n——  > ——\n      _\n==========\n/+++++++++|\n/+++++++|\nc c c c c c c c c")
elif fjotChosen == "dev":
    print("Entered Dev mode.")
# Pet Randomizer
pets = ["Ghwv", "Bghy", "Pupie","Floowey","Turtoy"]
pet = (random.choice(pets))
# Pet Randomizer
print("A wild", pet, "has decided to befriend you!")
print("You meet a shopkeeper.")
shopDialogues = ["Hello how are you?", "I am the shopkeeper.", "Hello Fjot.","Give me money!","How can I help you?"]
shopDialogue = (random.choice(shopDialogues))
print(shopDialogue, "\n|0-----0|\n|     -  |")
enter1 = input("Press ENTER to continue. ")
print("Take one of these to aid you in your journey!")
print("Shotgun, Shotgun Shells, Cooked Beef, Cooked Mutton, Bread.")
itemChosen1 = input("Which one would you like?\n>")
if itemChosen1 == "Shotgun":
    weapon1 = "Shotgun"
elif itemChosen1 == "Shotgun Shells":
    ammo1 = "Shotgun Shells"
elif itemChosen1 == "Cooked Beef":
    food1 = "Cooked Beef"
elif itemChosen1 == "Cooked Mutton":
    food1 = "Cooked Mutton"
elif itemChosen1 == "Bread":
    food1 = "Bread"
print("You started your adventure!")
time.sleep(1)
print("There’s a black mist given off by an evil ox man killing many fjots. You are the only fjot alive and you were received a letter from the ground, it says:")
print("Dear fellow fjot, this is your brother fjot writing you a letter to let you know i’m still alive. Please, help me, I’ve been without food for days. Please find me dear fjot. - fjot")
location = input("Where would you like to go? Available: Ox Field\n>")
if location == "Ox Field":
    print("You see many oxen... They have a weird flash in their eyes...")
input("Press ENTER to continue.")
print("You run away from the field...")
print("The wind sways and you receive a note entitled ''Ox Man Profile''")
time.sleep(1)
print("Inside of the note it says:The ox man is found in the Ox dimension, where he is in his castle guarding it.")

