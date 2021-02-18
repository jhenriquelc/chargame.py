import copy


class Board:
    def __init__(self, limits, player=[], barriers=[]):
        self.limits = limits
        self.barriers = barriers
        self.player = player

        # config
        self.player_char = 'i'
        self.empty_char = ' '
        self.barrier_char = 'ø'

    @property
    def out_list(self):
        cache = []
        line = 0
        column = 0
        buffer = ''
        while line < self.limits[1]:
            while(column < self.limits[0]):
                if [column, line] in self.barriers:
                    buffer += self.barrier_char
                elif [column, line] == self.player:
                    buffer += self.player_char
                else:
                    buffer += self.empty_char
                column += 1
            column = 0
            cache.append(buffer)
            buffer = ''
            line += 1
        return cache

    def draw(self):
        for line in self.out_list:
            print(line)

    def canmove(self, direction):
        moving = copy.deepcopy(self.player)
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

    def move(self, direction):
        if(direction == 'up'):
            if self.canmove('up'):
                self.player[1] -= 1
        elif(direction == 'right'):
            if self.canmove('right'):
                self.player[0] += 1
        elif(direction == 'down'):
            if self.canmove('down'):
                self.player[1] += 1
        elif(direction == 'left'):
            if self.canmove('left'):
                self.player[0] -= 1
