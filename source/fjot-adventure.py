#// Imports
import time, random

prompt = ">> "
energy = 9.0

#// Shidneka variables.
shidnekaRender = [
    "==========\n",
    " ' ___> ' \n",
    "==========\n",
    "|+++++++++|\n",
    "|+++++++++|\n",
    "c c c c c c\n"    
]

shidnekaAbils = [
    "\tVery fast and agile.\n",
    "\tGood memory. Helpful for puzzles. (Uses up 10 brain power)\n",
    "\tDodging.\n",
    "\tDashing. (Uses 2.5 energy)\n",
    "\tTeleport. (Uses 10 energy)\n",
    "\tGood at melee.\n"
]

shidnekaWeaknss = [
    "\tNot a lot of health.\n",
    "\tBad at range.\n",
]

#// @TODO: List out bghays variables.
bghaysRender = [
    "==========\n",
    " O  > O   \n",
    "   ___    \n",
    "==========\n",
    "=]UUUUUU[= \n",
    " IUUUUUUI \n",
]




print("Welcome to Fjot Adventures!")
print("Choose a fjot class to start:")

#// Print information about each fjot class. 
print("Shidneka: ")
for line in shidnekaRender:
    print(line)

fjotChosen = str(input("[1] Shidneka (extinct); [2] Bghaydsa (new);\n" + prompt))

#// Chosen stuff.
def fjotChosenString(fjotChosen):

    if (fjotChosen == "1"):
        fjotChosenStr = "Shidneka"
    elif (fjotChosen == "2"):
        fjotChosenStr = "Bghaydsa"
    elif (fjotChosen == "debug"):
        fjotChosenStr = "Debug"

    return fjotChosenStr

fjotChosenStr = fjotChosenString(fjotChosen);
print("You have chosen",fjotChosenString(fjotChosen))

if fjotChosenStr == "Shidneka":
    print("You are the last of your kind. Try to survive.")
elif fjotChosenStr == "Bghaydsa":
    print("You have many Fjot friends to support you in your journey.")
elif fjotChosenStr == "Debug":
    print("DEBUG MODE.\n")

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
print("You grab " + itemChosen1 + " on the way to aid you in your journey.")
print("You started your adventure!")
time.sleep(1)
