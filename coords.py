class Coord:
    def __init__(self, x=0, y=0):
        if type(x) == list:
            self.x = x[0]
            self.y = x[1]
        else:
            self.x = x
            self.y = y

    def move(self, direction):
        if(direction == 'up'):
            self.y -= 1
        elif(direction == 'right'):
            self.x += 1
        elif(direction == 'down'):
            self.y += 1
        elif(direction == 'left'):
            self.x -= 1
        elif(direction == 'ur'):
            self.y -= 1
            self.x += 1
        elif(direction == 'ul'):
            self.y -= 1
            self.x -= 1
        elif(direction == 'dr'):
            self.y += 1
            self.x += 1
        elif(direction == 'dl'):
            self.y += 1
            self.x -= 1

    @property
    def out_list(self):
        return [self.x, self.y]
