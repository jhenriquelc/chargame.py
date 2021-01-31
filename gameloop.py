# ! WORK IN PROGRESS !
from board import Board
from clear_screen import clear
from getch import getch

def gameloop(limits, start, barriers):
    board = Board(start, limits, barriers)
    print('Use WASD to move')
    while True:
        clear()
        board.draw()
        char = getch()
        if char.lower() == 's':
            board.actor.move('down')
        elif char.lower() == 'w':
            board.actor.move('up')
        elif char.lower == 'a':
            board.actor.move('left')
        elif char.lower == 'd':
            board.actor.move('right')
        continue

# TODO: find a *reasonable* way to not have to copy&paste draw() from class Board
def pre_draw(limits, actor_coords, barriers):
    line = 0
    column = 0
    buffer = ''
    while line < limits[0]: # draws all lines
        while(column < limits[1]): # draws all columns
            if [column, line] in barriers:
                buffer += '☒'
            elif [column, line] == actor_coords:
                buffer += 'o'
            else:
                buffer += '·'
            column += 1
        column = 0
        print(buffer)
        buffer = ''
        line += 1

def getlimits():
    while True:
        size = input('Set the size of the grid: ')
        if size == 'h':
            print('input two positive integers separated by space')
            continue
        try:
            size = size.split()
            # with the input separated into a list, convert expected items to integers
            size[0] = int(size[0])
            size[1] = int(size[1])
            if size[0] < 0 or size[1] < 0:
                raise IndexError('Grid size should be positive')
            else:
                if len(size) == 2:
                    return size
                else:
                    print('enter only two numbers')
        except:
            print('invalid input, try again')
            print('enter two positive integers separated by space.')
            continue

def getstart(limits):
    while(True):
        start = input('Enter the initial position of the actor: ')
        if start == 'h':
            print('input two positive integers separated by space')
            continue
        if start == 'p':
            pre_draw(limits, [], [])
            continue
        try:
            start = start.split()
            start[0] = int(start[0])
            start[1] = int(start[1])
            if start[0] < 0 or start[1] < 0:
                raise IndexError('Positions must be positive')
            elif start[0] >= limits[0] or start[1] >= limits[1]:
                raise IndexError('Actor position can\'t be outside the grid')
            else:
                if len(start) == 2:
                    return start
        except:
            print('invalid input, try again')
            print('enter two positive integers separated by space,')
            print('the coords given must fall inside the grid')
            continue

def getbarriers(limits, start): # TODO: implement functionality in getbarriers()
    barriers = []
    while True:
        print('leave blank to skip/stop')
        entry = input('Enter a barrier position: ')
        if entry == 'h':
            print('input two positive integers separated by space')
            continue
        if entry == 'p':
            pre_draw(limits, start, barriers)
            continue
        if entry == '':
            break

        try:
            entry = entry.split()
            entry[0] = int(entry[0])
            entry[1] = int(entry[1])
        except:
            print('invalid input, try again')
            print('enter two positive integers separated by space,')
            continue
        
        if len(entry) == 2:
            barriers.append(entry)
        else:
            print('Input only two numbers')
            continue
    return barriers

# TODO: walk through the process of creating a board with the user
if __name__ == '__main__' :    
    print('Input "h" for help')
    print('!THIS PART OF THE CODE IS IMCOMPLETE!')
    limits = getlimits()
    print('Input "p" to see how the board currently looks like')
    start = getstart(limits)
    barriers = getbarriers(limits, start)
    print(limits, start, barriers)
    gameloop(limits, start, barriers) # infinite loop