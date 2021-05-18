import copy
from coords import Coord


class Board:
    def __init__(self, limits, player=[], barriers=[], movables=[]):
        self.limits = Coord(limits)
        self.barriers = [Coord(item) for item in barriers]
        self.movables = [Coord(item) for item in movables]
        self.player = Coord(player)
        self.border = copy.deepcopy(self.limits)
        # do this once diagonal movement is back: self.border.mv('dr')
        self.border.mv('down')
        self.border.mv('right')
        self._zerozero = Coord([0, 0])

        # config
        self.player_char = 'i'
        self.empty_char = ' '
        self.barrier_char = '▯'
        self.movable_char = '*'
        self.wall_char = '│'
        self.lid_char = '─'
        self.top_right_char = '┐'
        self.top_left_char = '┌'
        self.bottom_right_char = '┘'
        self.bottom_left_char = '└'

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

        for y in range(self.border.y + 1):
            scan_line = ''
            for x in range(self.border.x + 1):
                # if on top left
                if x == 0 and y == 0:
                    scan_line += self.top_left_char
                # if on bottom left
                elif x == 0 and y == self.border.y:
                    scan_line += self.bottom_left_char
                # if on top right
                elif x == self.border.x and y == 0:
                    scan_line += self.top_right_char
                # if on bottom right
                elif x == self.border.x and y == self.border.y:
                    scan_line += self.bottom_right_char
                # if on a side
                elif x == 0 or x == self.border.x:
                    scan_line += self.wall_char
                # if on top or bottom
                elif y == 0 or y == self.border.y:
                    scan_line += self.lid_char
                # if in middle
                else:
                    scan_line += out_list[y - 1][x - 1]
            screen_list.append(scan_line)
        return screen_list

    def __str__(self):
        output = ''
        for line in self.out_pretty_list:
            output += line + '\n'
        return output

    def __repr__(self):
        output = ''
        for line in self.out_list:
            output += line + '\n'
        return output

    def can_move(self, obj, direction):
        _obj = copy.deepcopy(obj)
        _obj.mv(direction)
        in_barrier = _obj in self.barriers
        in_movable = _obj in self.movables
        out_of_range = _obj >= self.limits or _obj < self._zerozero
        if in_barrier or in_movable or out_of_range:
            return False
        else:
            return True

    def mv(self, obj, direction):
        me = self.what_is(obj)
        _obj = copy.deepcopy(obj)
        _obj.mv(direction)
        front = self.what_is(_obj)
        canmove = self.can_move(obj, direction)
        if me == 'player':
            # if trying to push
            if front == 'movable' and self.can_move(_obj, direction):
                self.movables[self.movables.index(_obj)].mv(direction)
                self.player.mv(direction)
            # if moving into nothing
            elif canmove:
                self.player.mv(direction)
            
        

    def mv_player(self, direction):
        self.mv(self.player, direction)


if __name__ == '__main__':
    board = Board(
        limits=[9, 3],
        player=[6, 1],
        barriers=[[0, 0], [0, 1], [1, 0]],
        movables=[[7, 1], [8, 1]])
    print(board)
    board.mv_player('right')
    print(board)
    board.mv_player('down')
    print(board)
    board.mv_player('right')
    print(board)
    board.mv_player('up')
    print(board)
    board.mv_player('right')
    print(board)
