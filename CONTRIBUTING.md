# Contributing
When making a commit, it is required that you do a pull request. When making a commit, keep these in mind:

- Variables should follow the camel case rule.
- Refer to the docs/ for reference.

## Adding art
The ascii art must be uploaded in the 16x16 format or at minimum, 8x8. Feel free to add art in the [art/](./art/) directory as long as it follows the wiki/docs as reference.

## Building
## Npy Version/C++ Version
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
### Windows
Same goes for windows.
```
> g++ -o fa.exe FA.cpp
```

## Py Version
Just run:

```
python3 FjotAdventure.py
```
