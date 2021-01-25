class player():
    def __init__(self, start):
        self.coords = start
    def move(self, direction, barriers):
        if(direction == 'u'):
            if((self.coords[1] + 1) in barriers):
                self.coords[1] += 1
                return self.coords
            else:
                return self.coords
        elif(direction == 'r'):
            if((self.coords[0] + 1) in barriers):
                self.coords[0] += 1
                return self.coords
            else:
                return self.coords
        elif(direction == 'd'):
            if((self.coords[1] - 1) in barriers):
                self.coords[1] -= 1
                return self.coords
            else:
                return self.coords
        elif(direction == 'l'):
            if((self.coords[0] - 1) in barriers):
                self.coords[0] -= 1
                return self.coords
            else:
                return self.coords
