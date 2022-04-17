#!/bin/python3

import copy
from readchar import readkey as getch
from coords import Coord
from clear_screen import clear


class Board:
    def __init__(self, limits, player=[], barriers=[], movables=[], goal=[]):
        self._limits = Coord(limits)
        self.barriers = [Coord(item) for item in barriers]
        self.movables = [Coord(item) for item in movables]
        self.player = Coord(player)
        self.goal = Coord(goal)
        self._border = copy.deepcopy(self._limits)
        self._border.mv('dr')
        self._zerozero = Coord([0, 0])

        self.chars = {
            'player': 'i',
            'empty': ' ',
            'out of bounds': '!',
            'barrier': '▯',
            'movable': '*',
            'goal': 'o',
            'wall': '│',
            'lid': '─',
            'top_right': '┐',
            'top_left': '┌',
            'bottom_right': '┘',
            'bottom_left': '└'
        }
        self.move_keys = {
            'w': 'up',
            'a': 'left',
            's': 'down',
            'd': 'right',
            'q': 'ul',
            'e': 'ur',
            'z': 'dl',
            'c': 'dr',
        }

    def what_is(self, coord):
        if coord.x >= self._limits.x or coord.y >= self._limits.y:
            return 'out of bounds'
        if coord in self.barriers:
            return 'barrier'
        elif coord == self.player:
            return 'player'
        elif coord in self.movables:
            return 'movable'
        elif coord == self.goal:
            return 'goal'
        else:
            return 'empty'

    @property
    def out_list(self):
        screen_list = []
        line = 0
        column = 0
        scan_line = ''
        while line < self._limits.y:
            while(column < self._limits.x):
                scan_line += self.chars[self.what_is(Coord(column, line))]
                column += 1
            column = 0
            screen_list.append(scan_line)
            scan_line = ''
            line += 1
        return screen_list

    @property
    def out_pretty_list(self) -> str:
        screen_list = []
        out_list = self.out_list

        for y in range(self._border.y + 1):
            scan_line = ''
            for x in range(self._border.x + 1):
                # if on top left
                if x == 0 and y == 0:
                    scan_line += self.chars['top_left']
                # if on bottom left
                elif x == 0 and y == self._border.y:
                    scan_line += self.chars['bottom_left']
                # if on top right
                elif x == self._border.x and y == 0:
                    scan_line += self.chars['top_right']
                # if on bottom right
                elif x == self._border.x and y == self._border.y:
                    scan_line += self.chars['bottom_right']
                # if on a side
                elif x == 0 or x == self._border.x:
                    scan_line += self.chars['wall']
                # if on top or bottom
                elif y == 0 or y == self._border.y:
                    scan_line += self.chars['lid']
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

    def can_move(self, obj: Coord, direction: str) -> bool:
        _obj = copy.deepcopy(obj)
        _obj.mv(direction)
        in_barrier = _obj in self.barriers
        in_movable = _obj in self.movables
        out_of_range = _obj >= self._limits or _obj < self._zerozero
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

    def play(self):
        clear()
        stopped = False
        won = False
        lost = False
        invalid_key = False
        print('Use WASD to move, K to exit')
        print(self)

        # bad loop lol
        while 1:
            print('Use WASD to move, K to exit')
            print(self)
            if invalid_key:
                print('Press a valid key')
                invalid_key = False
            else:
                print('')
            key = getch()
            if key == '\x03' or key == 'k':
                stopped = True
                break
            try:
                self.mv_player(self.move_keys[key])
            except:
                invalid_key = True
            clear()

            if self.goal in self.movables:
                lost = True
                break
            if self.player == self.goal:
                won = True
                break
        #TODO: Remove double ifs
        if lost:
            print('Try not doing this again')
            return False
        elif won:
            print('Congratulations')
            return True
        elif stopped:
            print('exiting...')
            return None


if __name__ == '__main__':
    board = Board(
        limits=[9, 3],
        player=[6, 1],
        barriers=[[0, 0], [0, 1], [1, 0]],
        movables=[[7, 1], [8, 1]],
        goal=[0, 2])
    board.play()
