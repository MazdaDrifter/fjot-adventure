# Fjot Adventures
Text based adventure RPG with a whole bunch of [stuff](./docs). Rendered in beautiful ASCII and written in Python.

![fjot adventures picture](./fjotAdventures.png)

## It's state
It is currently in a beta/pre-release state. The goal is to include all of the things in the [docs/](./docs) into the game.

## Contributors
- owowoowo, developer/creator
- asciifeather, developer/creator
- hai, brainstormer
- drift, brainstormer

## Running it
Fjot adventure works on linux, osx and windows as long as python3 is installed. 

Navigate to the source/ directory/folder of fjotadventure.py, then, run it.

```$ python3 fjotadventure.py```

*For more information about how to play the game read the [documentation](./docs)*

## Modded
Modded comes with it's own scripting language. Here's what adding a boss into the game might look like:

```
s Boss standard variables
b ExampleBossName
bhp 967 
bacc 56 
bst 100 
pua 3

s Boss String Variables 
pstr < This is a text message the boss will say >
bdesc < Boss Description > 
bart ( BossArt.ascii )
```

s - section, used for organizing code.

b - boss name

bhp - boss health

bacc - boss accuracy

bst - boss strength

pua - power ups accepted

pstr - text message/print string

bdesc - boss description

bart - boss art 

