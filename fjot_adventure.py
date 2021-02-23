# Imports
import time, random, fjot

prompt = ">> "

print("Welcome to Fjot Adventures!")
print("Choose a fjot:")
fjotChosen = str(input("[1] Shidneka (extinct); [2] Bghaydsa (new);\n" + prompt))

def fjotChosenString(fjotChosen):

    if (fjotChosen == "1"):
        fjotChosenStr = "Shidneka"
    elif (fjotChosen == "2"):
        fjotChosenStr = "Bghaydsa"
    
    return fjotChosenStr

print("You have chosen",fjotChosenString(fjotChosen))
if fjotChosen == "":
    print("You are the last of your kind. Try to survive.\n——  > ——\nO-----O\n==========\n/+++++++++|\n /+++++++|\nu u u u u u u u u")
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
print("Dagger, Carrots, Cooked Mutton, Bread.\n")
itemChosen1 = input("Which one would you like? (Pick wisely)\n" + prompt)
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
# letter
# \t = indent 
letter = [
            "\n\tDear fellow fjot, this is your brother, \n"
            "\tfjot, here to tell you i'm still alive. \n"
            "\tHiding from the unearthly foul of this mist.\n"
            "\tPlease rescue me and deliver me to good health.\n"
            "\tSincerely, fjot 430\n"
         ]

# Print letter
for line in letter:
    print(line)

flash = [
            "||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n",
            "||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n",
            "||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n",
            "||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n",
            "||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n",
            "||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n",
            "||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n",
            "||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n",
            "||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n",
            "||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n",
            "||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n",
            "||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n",
            "||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n",
            "||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n",
            "||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n"
        ]

input("Press ENTER to continue.")
print("You take a nap...")
time.sleep(3)
print("You see many oxen...\nThey have a weird flash in their eyes...")
input("Press ENTER to continue.")

for line in flash:
    print(line)

input("Press ENTER to continue.")
print("You run away from the field...")
print("You wake up realizing it was all a dream.")
print("The wind sways and you receive a note entitled ''Ox Man Profile''")
input("Press ENTER to continue.")
print("Inside of the note it says: \n\tThe ox man is found in the Ox dimension, where he is in his castle guarding it.")

print("You pack your things and ride your bike.")
print("You find a village. Would you like to explore it?")

io = str(input("Yes [1]; No [2];\n" + prompt))

if "1" in io:
    print("You start exploring the village.")    
elif "2" in io:
    print("You continue on.")

