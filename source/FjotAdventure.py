# New Edition. See archives/ for an older version.
# Author: asciiFeather
# About File: Stores the titlescreen and runs the specific version.
import time, platform, random
from Components import Reader, Cmd, Section
from Entities import Fjot

from os import system, name

# Ref: https://www.geeksforgeeks.org/clear-screen-python/
def clear():
    # Windows
    if name == 'nt':
        system('cls')
    # *nix
    else:
        system('clear')


# ReaderComponent - accepts a filepath.
scene = Reader.ReaderComponent('../art/titlescreen.ascii')
options = Reader.ReaderComponent('../text/titlescreen_options.txt')
prompt = '>'

# SectionComponent - accepts a seperator string.
sect = Section.SectionComponent('+============================================================================+')

# First, clear the screen.
clear()

# +====================+
#    Scene Section.
# +====================+
sect.startDrawingSection()

scene.output() # draw scene

sect.endDrawingSection()


# +====================+
#    Options Section.
# +====================+
sect.startDrawingSection()

options.output()

sect.endDrawingSection()

# End