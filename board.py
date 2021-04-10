import copy
from coords import Coord


class Board:
    def __init__(self, limits, player=[], barriers=[], movables=[]):
        self.limits = Coord(limits)
        self.barriers = [Coord(item) for item in barriers]
        self.movables = [Coord(item) for item in movables]
        self.player = Coord(player)
        # config
        self.player_char = 'i'
        self.empty_char = ' '
        self.barrier_char = 'ø'
        self.movable_char = '*'
        self.corner_char = '#'
        self.wall_char = '|'
        self.lid_char = '-'

    def what_is(self, coord):
        if coord.x >= self.limits.x or coord.y >= self.limits.y:
            return 'out of bounds'
        if coord in self.barriers:
            return 'barrier'
        elif coord == self.player:
            return 'player'
        elif coord in self.movables:
            return 'movable'
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
                if Coord([column, line]) in self.barriers:
                    scan_line += self.barrier_char
                elif Coord([column, line]) == self.player:
                    scan_line += self.player_char
                elif Coord([column, line]) in self.movables:
                    scan_line += self.movable_char
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

    def __str__(self):
        output = ''
        for line in self.out_list:
            output += line + '\n'
        return output

    def __repr__(self):
        output = ''
        for line in self.out_pretty_list:
            output += line + '\n'
        return output

    def can_move(self, obj, direction):
        _obj = copy.deepcopy(obj)
        _obj.mv(direction)
        in_barrier = _obj in self.barriers
        in_movable = _obj in self.barriers
        out_of_range = _obj.x >= self.limits.x or _obj.y >= self.limits.y
        if in_barrier or in_movable or out_of_range:
            return False
        else:
            return True

    def mv(self, obj, direction):
        _obj = copy.deepcopy(obj)
        _obj.mv(direction)
        if self.what_is(obj) == 'movable' and self.can_move(obj, direction):
            obj.mv(direction)
        elif self.what_is(obj) == 'player' and self.what_is(_obj) == 'movable':
            if self.can_move(_obj, direction):
                index = self.movables.index(_obj)
                _obj.mv(direction)
                self.movables[index] = _obj
                obj.mv(direction)
        elif self.what_is(obj) == 'player' and self.can_move(obj, direction):
            obj.mv(direction)

    def mv_player(self, direction):
        self.mv(self.player, direction)


if __name__ == '__main__':
    board = Board(
        limits=[9, 3],
        player=[6, 1],
        barriers=[[0, 0], [0, 1], [1, 0]],
        movables=[[7, 1]])
    print(repr(board))
    board.mv_player('right')
    print(repr(board))
    board.mv_player('down')
    board.mv_player('right')
    print(repr(board))
    board.mv_player('up')
    print(repr(board))
