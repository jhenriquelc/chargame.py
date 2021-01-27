from actor import Actor

class Board:
    def __init__(self, start, limits, barriers):
        self.limits = limits
        self.actor = Actor(start, limits, barriers)
        self.barriers = barriers
    
    def draw(self):
        line = 0
        collumn = 0
        buffer = ''
        while line < self.limits[0]:
            while(collumn < self.limits[1]):
                if [collumn, line] in self.barriers:
                    buffer += '☒'
                elif [collumn, line] == self.actor.coords:
                    buffer += 'o'
                else:
                    buffer += '·'
                collumn += 1
            collumn = 0
            print(buffer)
            buffer = ''
            line += 1

# TODO: walk through the process of creating a board with the user
if __name__ == 'main' :
    print('Input "h" for help')
    
    # defines grid size
    while(True): # break on line 45
        size = input('Set the size of the grid: ')
        # errors expected from user input xd
        try:
            if size == 'h':
                print('input two positive integers separated by space')
                continue
            size = size.split()
            # with the input separated into a list, convert expected items to integers
            size[0] = int(size[0])
            size[1] = int(size[1])
            if size[0] < 0 or size[1] < 0:
                raise IndexError('Grid size should be positive')
            else:
                break
        except:
            print('invalid input')
            print('enter two positive integers separated by space.')
            continue
    print(size)
    
        