# Contributing
When making a commit, you must pull request. These are some of the regulations you shall follow:

- Variables should follow the camel case rule.
- Look at [docs/](./docs) for reference.

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
