class Board:
    def __init__(self, start, limits, barriers):
        from actor import Actor
        self.limits = limits
        self.actor = Actor(start, limits, barriers)
        self.barriers = barriers
    
    def draw(self):
        line = 0
        column = 0
        buffer = ''
        while line < self.limits[1]:
            while(column < self.limits[0]):
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