# Screep Typing for Python

## Intentions

If Screeps ever gets any form of Python interface, there will need to be something to differentiate between a dictionary and a class, as Java (the language Screeps intends you to write in) does not differentiate between them. This aims to provide the typing for this conversion, not the actual mechanics.

## Road Map

1. [`raw.py`](raw.py) is, as the name suggests, a very raw form of the end goal. It will raise errors when run, as many objects are undefined (as it is still being written) and many objects are defined out of order. Once the entirety of the [screeps api](https://docs.screeps.com/api) is stored into [`raw.py`](raw.py), the next step can begin.
2.  [`main.py`](main.py), once it is created, will contain a more functional version of the contents of [`raw.py`](raw.py). This will lack any type definitions for in-code inputs, but may still raise errors due to functions from a class returning an instance of that class (e.g. `MapVisual.circle()` returns the `MapVisual` object), as the class is in the process of being defined.

## How you can help

If you want to help, check out any issues and propose/create a pull request for fixes.
