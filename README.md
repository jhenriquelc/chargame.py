
# coords-py

A shitty top-down view board with a thingy you can move made in python to work in the terminal

  

I'm currently having problems with movement. Any help is more than enough.

  

*Please only use my code if you're going to make your program free and open-source too, thanks. (I'm not enforcing it)*

  

## How-to

  

### Board

The `Board` class creates a grid with customizable size, barriers (experimental), and an `Actor` object.

  

The Actor object holds a position (``Actor.coords``) and a function to move it (``Actor.move()``) which requires an direction represented by a string with its name.

Example: ``Actor.move('left')``

  

*All attributes and methods are made for tinkering, don't be shy!*

  

`board.draw()` writes the board line by line on the terminal, currently working on a way for the results to be returned by a function instead of printed

  

#### Coords

Coordinates are represented by a list with two numbers, line and column.

An example: ``board.actor.coords = [5, 3]`` .

  

*Lines are counted from top to bottom and begin with 0.*

#### Barriers list

Barriers are contained in a list of coords.

Example: `` barriers = [[4, 5], [1, 4], [0, 3]]`` .