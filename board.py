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

        self.corner_char = '#'
        self.wall_char = '|'
        self.lid_char = '-'

    @property
    def ylimit(self):
        return self.limits[1]

    @property
    def xlimit(self):
        return self.limits[0]

    @property
    def out_list(self):
        cache = []
        line = 0
        column = 0
        buffer = ''
        while line < self.ylimit:
            while(column < self.xlimit):
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

    @property
    def out_pretty_list(self):
        cache = []
        out_list = self.out_list
        for y in range(self.ylimit + 2):
            buffer = ''
            for x in range(self.xlimit + 2):
                # if on top or bottom
                if y == 0 or y == self.ylimit + 1:
                    # and on the sides, aka on a corner
                    if x == 0 or x == self.xlimit + 1:
                        buffer += self.corner_char
                    # on top or bottom, but not on a side
                    else:
                        buffer += self.lid_char
                # if not on top on bottom, but on a side
                elif x == 0 or x == self.xlimit + 1:
                    buffer += self.wall_char
                # if on middle
                else:
                    buffer += out_list[y - 1][x - 1]
            cache.append(buffer)
        return cache

    def draw(self):
        for line in self.out_pretty_list:
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
        pastx = moving[0] >= self.xlimit
        pasty = moving[1] >= self.ylimit
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
