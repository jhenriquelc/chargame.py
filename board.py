from actor import Actor

class Board:
    def __init__(self, start, limits, barriers):
        self.limits = limits
        self.actor = Actor(start, limits, barriers)
        self.barriers = barriers
    
    def draw(self):
        line = 0
        column = 0
        buffer = ''
        while line < self.limits[0]:
            while(column < self.limits[1]):
                if [column, line] in self.barriers:
                    buffer += '☒'
                elif [column, line] == self.actor.coords:
                    buffer += 'o'
                else:
                    buffer += '·'
                column += 1
            column = 0
            print(buffer)
            buffer = ''
            line += 1

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
    while(True): # break on line 42
        size = input('Set the size of the grid: ')
        if size == 'h':
            print('input two positive integers separated by space')
            continue
        # errors expected from user input xd
        try:
            size = size.split()
            # with the input separated into a list, convert expected items to integers
            size[0] = int(size[0])
            size[1] = int(size[1])
            if size[0] < 0 or size[1] < 0:
                raise IndexError('Grid size should be positive')
            else:
                break
        except:
            print('invalid input, try again')
            print('enter two positive integers separated by space.')
            continue
    return size

def getstart(limits):
    while(True):
        start = input('Enter the initial position of the actor: ')
        if start == 'h':
            print('input two positive integers separated by space')
            continue
        if start == 'p':
            pre_draw(limits, [], [])
            continue
        # errors expected from user input… again.̣
        try:
            start = start.split()
            start[0] = int(start[0])
            start[1] = int(start[1])
            if start[0] < 0 or start[1] < 0:
                raise IndexError('Positions must be positive')
            elif start[0] >= limits[0] or start[1] >= limits[1]:
                raise IndexError('Actor position can\'t be outside the grid')
            else:
                break
        except:
            print('invalid input, try again')
            print('enter two positive integers separated by space,')
            print('the coords given must fall inside the grid')
    return start

def getbarriers(limits, start): # TODO: implement functionality in getbarriers()
    return []

# TODO: walk through the process of creating a board with the user
if __name__ == '__main__' :    
    print('Input "h" for help')
    print('!THIS PART OF THE CODE IS IMCOMPLETE!')
    limits = getlimits()
    print('Input "p" to see how the board currently looks like')
    start = getstart(limits)
    barriers = getbarriers(limits, start)
    print(limits, start, barriers)