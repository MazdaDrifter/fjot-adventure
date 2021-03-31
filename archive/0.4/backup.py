print("There’s a black mist given off by an evil ox man killing many fjots. You are the only fjot alive and you were receive
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