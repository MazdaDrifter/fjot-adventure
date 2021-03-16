def listUI(health, energy, stamina, hunger, thirst):
        #// Take in params (health, energy, stamina, hunger, thirst) and display out.
        #// str() function converts the ints to strings.
        ui_listing = [
            "Health: " + str(health),
            "Energy: " + str(energy),
            "Stamina: " + str(stamina),
            "Hunger: " + str(hunger),
            "Thirst: " + str(thirst)
        ]
        for sect in ui_listing:
            print(sect)
