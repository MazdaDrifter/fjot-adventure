#// Command prompt functions.
#// See COMMANDS.txt for more info.
import ui, fjot


def doCommands(command, fjotInstance):
    if command == 'ds':
        ui.listUI( fjotInstance.health, 
            fjotInstance.energy, 
            fjotInstance.hunger,
            fjotInstance.thirst )
    #// @TODO: Add dbs function.
    elif command == 'dg':
        print("You dodge.")
    elif command == 't':
        print("You teleport.")
    elif command == 'u':
        print("You move up.")
    elif command == 'd':
        print("You move down.")
    elif command == 'r':
        print("You move right.")
    elif command == 'l':
        print("You move left")
    elif command == 'a':
        print("You attack.")
