# Contributing
When making a commit, it is required that you do a pull request. Pull requests are great for reviewing code of yours, and is a good way to keep this repository maintained. Once your pull request has been accepted your code can now be properly merged with the master branch.

## For developers
When developing code in the repo, please remember to:

- Follow camel case naming rules.
- Comment what the file is about.
- Please make the variables and functions names clearly understandable.

## Adding art
The ascii art must be uploaded in the 16x16 format or at minimum, 8x8. Feel free to add art in the [art/](./art/) directory as long as it follows the wiki/docs as reference. Feel free to also add your own art which might be added into the game as long as it is not vulgar and offensive.

## Building
## Npy Version/C++ Version (Please update for Windows)
Dependencies needed:

```
g++
```

### MacOS
```
$ g++ -o fa.exe FA.cpp
```

### Linux 
Navigate to the fjot-adventure/npyfound/script directory. Compile.
```
$ g++ -o fa FA.cpp
```

## Py Version
Just run:

```
python3 FjotAdventure.py
```
