#// Imports
import time
import random
import colorama
from colorama import Fore
from colorama import Style
from colorama import Back
#// Fjot adventure modules.
import renderer
import ui
import convert
import command
import fjot

prompt = ">> "

#// Shidneka variables.
shidnekaAbils = [
    "\tVery fast and agile.\n",
    "\tGood memory. Helpful for puzzles (Uses up 10 brain power)\n",
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



title = [
    "||||||||||||||      |||VVVVVVVV|||     ",
    "|||                 |||        |||     ",
    "||||||||||||||      |||VVVVVVVV|||     ",
    "|||                 |||        |||     ",
    "|||                 |||        |||     ",
    "|||                 |||        |||     ",
    "|||                 |||        |||     ",
    "|||                 |||        |||     ",
    "|||             o   |||        |||   o "
]
#// Reference: https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
for line in title:
    print(Fore.CYAN + line)
print(Style.RESET_ALL)
time.sleep(2)
print("Choose a fjot class to start:")

#// Print information about each fjot class. 
print("Shidneka: \n")
renderer.render("../art/shidneka.ascii")
print("Bghays: \n")
renderer.render("../art/bghays.ascii")
fjotChosen = str(input("[1] Shidneka (extinct); [2] Bghaydsa (new);\n" + prompt))

#// Chosen stuff.
fjotChosenStr = convert.fjotChosenString(fjotChosen);
print("You have chosen",convert.fjotChosenString(fjotChosen))

if fjotChosenStr == "Shidneka":
    print("You are the last of your kind. Try to survive.")
elif fjotChosenStr == "Bghaydsa":
    print("You have many Fjot friends to support you in your journey.")
elif fjotChosenStr == "Debug":
    print("")

# Pet Randomizer
pets = ["Ghwv", "Bghy", "Pupie","Floowey","Turtoy"]
pet = (random.choice(pets))

print("A wild", pet, "has decided to befriend you!")
print("You meet a shopkeeper.")
shopDialogues = ["Hello how are you?", "I am the shopkeeper.", 
"Salutations!", "Goodday!", "How can I help you?"]
shopDialogue = random.choice(shopDialogues)

print("[Shopkeeper]: " + shopDialogue)
renderer.render("../art/shopkeeper.ascii")

input("Press ENTER to continue. ")

print("[Shopkeeper]: Take one of these to aid you in your journey!")

shopContents = [
                "1. Crude Stone Sword\n",
                "2. Carrot seeds\n",
                "3. Cooked Mutton.\n",
                "4. Bread.\n"
               ]

#// Print shopContents list.
for line in shopContents:
    print(line)

itemChosen1 = input("Which one would you like? (Pick wisely)\n" + prompt)

#// Chosen stuff.
print("You grab " + convert.itemChosenToStr(itemChosen1) + " on the way to aid you in your journey.")
print("You start your adventure!")
time.sleep(1)

mineralsPossible = ["iron", "copper"]
randMineralFound = (random.choice(mineralsPossible))

print("You find", randMineralFound, "laying on the ground.")


