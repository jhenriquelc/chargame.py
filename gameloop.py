from board import Board
from clear_screen import clear
from getch import getch


def main():
    print('Input "h" for help')
    board = Board(getlimits())
    print('Input "p" to see how the board currently looks like')
    board.player = getstart(board)
    getbarriers(board)
    gameloop(board)  # infinite loop


def gameloop(board):
    print('Use WASD to move')
    while True:
        clear()
        board.draw()
        char = getch()
        if char.lower() == 's':
            board.move('down')
        elif char.lower() == 'w':
            board.move('up')
        elif char.lower() == 'a':
            board.move('left')
        elif char.lower() == 'd':
            board.move('right')
        continue


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


def getstart(board):
    while(True):
        start = input('Enter the initial position of the player: ')
        if start == 'h':
            print('input two positive integers separated by space')
            continue
        if start == 'p':
            board.draw()
            continue
        try:
            start = start.split()
            start[0] = int(start[0])
            start[1] = int(start[1])
            if start[0] < 0 or start[1] < 0:
                raise IndexError('Positions must be positive')
            elif start[0] >= board.limits[0] or start[1] >= board.limits[1]:
                raise IndexError(
                    'Actor position can\'t be outside the grid')
            else:
                if len(start) == 2:
                    return start
        except:
            print('invalid input, try again')
            print('enter two positive integers separated by space,')
            print('the coords given must fall inside the grid')
            continue


def getbarriers(board):
    board.barriers = []
    while True:
        print('leave blank to skip/stop')
        entry = input('Enter a barrier position: ')
        if entry == 'h':
            print('input two positive integers separated by space')
            continue
        if entry == 'p':
            board.draw()
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
            board.barriers.append(entry)
        else:
            print('Input only two numbers')
            continue


if __name__ == '__main__':
    main()
