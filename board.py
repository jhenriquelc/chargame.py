class Board:
    def __init__(self, start, limits, barriers):
        from actor import Actor
        self.limits = limits
        self.actor = Actor(start, limits, barriers)
        self.barriers = barriers
    
    @property
    def out_list(self):
        cache = []
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
            cache.append(buffer)
            buffer = ''
            line += 1
        return cache
    
    def draw(self):
        for line in self.out_list:
            print(line)