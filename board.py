import copy
from coords import Coord


class Board:
    def __init__(self, limits, player=[], barriers=[]):
        self.limits = Coord(limits)
        self.barriers = [Coord(item) for item in barriers]
        self.player = Coord(player)
        self.barrier_list = [item.out_list for item in self.barriers]

        # config
        self.player_char = 'i'
        self.empty_char = ' '
        self.barrier_char = 'ø'
        self.corner_char = '#'
        self.wall_char = '|'
        self.lid_char = '-'

    def whats_in(self, coord):
        _coord = coord.out_list
        if coord.x >= self.limits.x or coord.y >= self.limits.y:
            return False
        if _coord in self.barrier_list:
            return 'barrier'
        elif _coord == self.player.out_list:
            return 'player'
        else:
            return 'empty'

    @property
    def out_list(self):
        screen_list = []
        line = 0
        column = 0
        scan_line = ''
        while line < self.limits.y:
            while(column < self.limits.x):
                if [column, line] in self.barrier_list:
                    scan_line += self.barrier_char
                elif [column, line] == self.player.out_list:
                    scan_line += self.player_char
                else:
                    scan_line += self.empty_char
                column += 1
            column = 0
            screen_list.append(scan_line)
            scan_line = ''
            line += 1
        return screen_list

    @property
    def out_pretty_list(self):
        screen_list = []
        out_list = self.out_list
        for y in range(self.limits.y + 2):
            scan_line = ''
            for x in range(self.limits.x + 2):
                # if on top or bottom
                if y == 0 or y == self.limits.y + 1:
                    # and on the sides, aka on a corner
                    if x == 0 or x == self.limits.x + 1:
                        scan_line += self.corner_char
                    # on top or bottom, but not on a side
                    else:
                        scan_line += self.lid_char
                # if not on top on bottom, but on a side
                elif x == 0 or x == self.limits.x + 1:
                    scan_line += self.wall_char
                # if on middle
                else:
                    scan_line += out_list[y - 1][x - 1]
            screen_list.append(scan_line)
        return screen_list

    def draw(self):
        for line in self.out_pretty_list:
            print(line)
    
    def can_move(self, obj, direction):
        return True #TODO: implement move checks

    def move(self, obj, direction):
        _obj = copy.deepcopy(obj)
        _obj.move(direction)
        if self.whats_in(obj) == 'player' and self.whats_in(_obj) == 'movable':
            pass #TODO: implement movable objects
        elif self.whats_in(obj) == 'movable':
            pass #NOTE: here too!
        elif self.whats_in(_obj) == 'empty':
            obj.move(direction)
        