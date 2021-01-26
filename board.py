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
