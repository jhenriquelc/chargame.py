# chargame.py

## Coordinates
Coordinates are represented by a list with two positive integers, with the first being the X coordinate and the second being Y. Example: `[5, 7]`

When on-screen, the Y coordinate increases the more it moves down, just like in a CRT line counter.

## Board
The `Board` class is a grid with customizable size, barriers, a player, its functions and attributes.

#### Initializating
The only variable needed during class initialization is the grid size, this can be changed on the fly. Others can be set during initialization and can be added/changed on the fly too.
 * Limits sets the size of the grid
  * For a 9x3 grid use `Board([9, 3])`
 * Player is the initial location of the player
 * Barriers is a list containing coordinates, a list of lists of integers.
  * Example: `[[0, 0], [9, 3], [7, 2]]`


#### Board's functions and attributes
 * `out_list` returns a list of strings, each string is a line, representing the whole board, but in slices.
 * `out_pretty_list` does about the same as `out_list`, but when printed line by line can be more appealing to the eye. Decoration is configurable.
 * `draw()` draws the result from `out_pretty_list` line by line.
 * `canmove(direction)` returns True or False based on the possibility of player movement on the specified directions. Directions include 'up', 'down', 'left', and 'right'.
 * `move(direction)` moves in the specified direction if `canmove()` returns True.
 * `ylimit` and `xlimit`return `self.limits[1]` and `self.limits[0]` respectively, made for better readability

## Gametest
Gametest requires pip modules `getch` and `clear_screen`.
It is an example on what is possible with this code, try it out!
