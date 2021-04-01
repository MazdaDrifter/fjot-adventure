# Component Reference / Easy access modules of the game
Components for building a scene and it's functions.

- ReaderComponent - Accepts a filepath and outputs the contents of a file. Example:

```py
from Components import Reader

# Read shidneka.ascii
readerInstance = Reader.ReaderComponent('art/shidneka.ascii')

# Output the content of the file.
readerInstance.output()
```

- SectionComponent - Accepts a separator and makes a section. Example:

```py
from Components import Section

# Where ---- is an example of a separator.
sectionInstance = Section.SectionComponent('----') 

# Start the section.
sectionInstance.startDrawingSection()

# Functions inside the section.

sectionInstance.endDrawingSection() # End the section.
```
