#// Convert no. choices to strings
def fjotChosenString(fjotChosen):

    if (fjotChosen == "1"):
        fjotChosenStr = "Shidneka"
    elif (fjotChosen == "2"):
        fjotChosenStr = "Bghaydsa"
    elif (fjotChosen == "0"): 
        fjotChosenStr = "Debug"

    return fjotChosenStr


def itemChosenToStr(itemChosen1):

    if (itemChosen1 == "1"):
        itemChosenStr = "a crude stone sword"
    elif (itemChosen1 == "2"):
        itemChosenStr = "carrot seeds"
    elif (itemChosen1 == "3"):
        itemChosenStr = "cooked mutton"
    elif (itemChosen1 == "4"):
        itemChosenStr = "bread"

    return itemChosenStr
