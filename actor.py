class Actor():
    def __init__(self, start, limits, barriers):
        self.coords = start
        self.limits = limits
        self.barriers = barriers
    
    def canmove(self, direction):
        moving = self.coords
        if(direction == 'up'):
            moving[1] -= 1
        elif(direction == 'right'):
            moving[0] += 1
        elif(direction == 'down'):
            moving[1] += 1
        elif(direction == 'left'):
            moving[0] -= 1
        
        if((moving[0] > self.limits[0]) or (moving[1] > self.limits[1]) or (-1 in moving) or (moving in self.barriers)):
            return False
        else:
            return True

    def move(self, direction):
        if(direction == 'up'):
            if self.canmove('up'):
                self.coords[1] -= 1

        elif(direction == 'right'):
            if self.canmove('right'):
                self.coords[0] += 1
        elif(direction == 'down'):
            if self.canmove('down'):
                self.coords[1] += 1
        elif(direction == 'left'):
            if self.canmove('left'):
                self.coords[0] -= 1