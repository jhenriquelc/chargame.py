import copy

class Actor():
    def __init__(self, start, limits, barriers):
        self.coords = start
        self.limits = limits
        self.barriers = barriers
    
    # returns True if all validations are False
    # TODO: Test if collisions are working as expected
    def canmove(self, direction):
        moving = copy.deepcopy(self.coords)
        if(direction == 'up'):
            moving[1] -= 1
        elif(direction == 'right'):
            moving[0] += 1
        elif(direction == 'down'):
            moving[1] += 1
        elif(direction == 'left'):
            moving[0] -= 1
        
        # validations
        onbarrier = moving in self.barriers
        pastx = moving[0] >= self.limits[0]
        pasty = moving[1] >= self.limits[1]
        negative = -1 in moving
        blocked = moving in self.barriers
        
        if(onbarrier or pastx or pasty or negative or blocked):
            return False
        else:
            return True

    # attempts to move in a specified direction
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