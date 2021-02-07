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
import random
pets = ["Ghwv", "Bghy", "Pupie'","Floowey","Turtoy"]
pet = (random.choice(pets))
# Pet Randomizer