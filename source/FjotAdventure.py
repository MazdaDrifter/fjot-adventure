# New Edition. See archives/ for an older version.
# About File: Stores the titlescreen and runs the specific version.
import time, platform, random
from Components import Reader, Cmd, Section
from Entities import Fjot

# ReaderComponent - accepts a filepath.
scene = Reader.ReaderComponent('art/titlescreen.ascii')
options = Reader.ReaderComponent('text/titlescreen_options.txt')
prompt = '>'

# SectionComponent - accepts a seperator string.
sect = Section.SectionComponent('+============================================================================+')

# +====================+
#    Scene Section.
# +====================+
sect.startDrawingSection()

scene.output() # draw scene

sect.endDrawingSection()


# +====================+
#    Options Section.
# +====================+
