from __future__ import print_function
import itertools
import copy
import time

start_file = open('./aoc_day_11_input.txt')
instructions = start_file.read().strip().splitlines()



floors1 = [['pog', 'thg', 'thm', 'prg', 'rug', 'rum', 'cog', 'com'], ['pom', 'prm'],[],[]]
floors2 = [['pog', 'thg', 'thm', 'prg', 'rug', 'rum', 'cog', 'com', 'elm', 'elg', 'dim', 'dig'], ['pom', 'prm'],[],[]]
game2amt = 14
game1amt = 10


class Game(object):

    def __init__(self, floor_plan, moves, elevator_floor, end_amt):
        self.floor_plan = floor_plan
        self.moves = moves
        self.elevator_floor = elevator_floor
        self.end_amt = end_amt


    def is_valid_pair(self, pair):
        el1, el2 = pair
        if el1[-1] == 'g' and 'g' == el2[-1] or el1[:-1] == el2[:-1]:
            return True
        return False

    def has_only_pairs(self, floor):
        if len(self.floor_plan[floor]) == 0 or len(self.floor_plan[floor]) % 2 != 0:
            return False
        else:
            self.floor_plan[floor] = sorted(self.floor_plan[floor])
            for i in range(0, len(self.floor_plan[floor]), 2):
                if self.floor_plan[floor][i][:-1] != self.floor_plan[floor][i + 1][:-1]:
                    return False
            return True

    def get_pairs_to_move(self):
        pairs = []
        if len(self.floor_plan[self.elevator_floor]) == 2 and self.elevator_floor < 3 and self.can_move_up_two(self.floor_plan[self.elevator_floor]):
            pairs = [self.floor_plan[self.elevator_floor]]
        elif self.has_only_pairs(self.elevator_floor) and self.elevator_floor < 3 and self.can_move_up_two(self.floor_plan[self.elevator_floor]):
            return [[self.floor_plan[self.elevator_floor][0], self.floor_plan[self.elevator_floor][1]]]
        else:
            for pair in itertools.combinations(self.floor_plan[self.elevator_floor], 2):
                if self.is_valid_pair(pair) and self.can_move_up_two(pair):
                        pairs += [pair]
        return sorted(pairs, key = lambda x: (x[0], x[1][::-1]))

    def can_move_up_two(self, pair):
        if len(self.floor_plan[self.elevator_floor]) < 2 or self.elevator_floor == 3:
            return False
        return self.is_valid_floor([el for el in self.floor_plan[self.elevator_floor] if el not in pair]) \
               and self.is_valid_floor(self.floor_plan[self.elevator_floor + 1] + list(pair))

    def can_move_down_one(self, element):
        if self.elevator_floor == 0:
            return False
        return self.is_valid_floor([el for el in self.floor_plan[self.elevator_floor] if el != element]) \
                and self.is_valid_floor(self.floor_plan[self.elevator_floor - 1] + [element])

    def get_elements_to_move_down(self):
        elements = []
        if len(self.floor_plan[self.elevator_floor]) == 2 and self.is_valid_pair(self.floor_plan[self.elevator_floor]):
            elements = [sorted(self.floor_plan[self.elevator_floor])[0]]
        elif len(self.floor_plan[self.elevator_floor]) == 1:
            return self.floor_plan[self.elevator_floor]
        elif self.elevator_floor == 3 and len(self.floor_plan[3]) % 2 == 1 and len(self.floor_plan[1]) == 1:
            elements = [el for el in self.floor_plan[3] if el[:-1] == self.floor_plan[1][0][:-1]]
        else:
            for el in self.floor_plan[self.elevator_floor]:
                if self.can_move_down_one(el):
                        elements += [el]
        return elements



    @staticmethod
    def move(floor_plan, items, old_floor, new_floor):
        for item in items:
            floor_plan[old_floor].remove(item)
            floor_plan[new_floor].append(item)
        return floor_plan

    def has_only_pairs_on_last_floor(self):
        return self.elevator_floor == 3 and len(self.floor_plan[3]) >= 4 and self.has_only_pairs(3) and self.has_only_pairs(0)

    def process_turn(self):
        if self.is_done():
            print(self.moves)
            exit(0)
        if self.has_only_pairs_on_last_floor():
            pair = sorted([self.floor_plan[3][0], self.floor_plan[3][1]])
            new_floor_plan = copy.deepcopy(self.floor_plan)
            Game.move(new_floor_plan, pair, 3, 2)
            Game.move(new_floor_plan, (pair[0],), 2, 1)
            new_game = Game(new_floor_plan, self.moves + 2, self.elevator_floor - 2, self.end_amt)
            print(new_game)
            new_game.process_turn()
        elif self.elevator_floor == 2 and self.has_only_pairs(2) and self.has_only_pairs(3) and len(self.floor_plan[0]) != 0:
            el = sorted(self.floor_plan[2])[0]
            new_floor_plan = copy.deepcopy(self.floor_plan)
            Game.move(new_floor_plan, (el,), 2, 1)
            new_game = Game(new_floor_plan, self.moves + 1, self.elevator_floor - 1, self.end_amt)
            print(new_game)
            new_game.process_turn()

        else:
            pairs_up = self.get_pairs_to_move()
            if(len(pairs_up)) > 0:
                for pair in pairs_up:
                    new_floor_plan = copy.deepcopy(self.floor_plan)
                    Game.move(new_floor_plan, pair, self.elevator_floor, self.elevator_floor + 1)
                    new_game = Game(new_floor_plan, self.moves + 1, self.elevator_floor + 1, self.end_amt)
                    print(new_game)
                    new_game.process_turn()
            else:
                elements_down = self.get_elements_to_move_down()
                for el in elements_down:
                    new_floor_plan = copy.deepcopy(self.floor_plan)
                    Game.move(new_floor_plan, (el,), self.elevator_floor, self.elevator_floor - 1)
                    new_game = Game(new_floor_plan, self.moves + 1, self.elevator_floor - 1, self.end_amt)
                    print(new_game)
                    new_game.process_turn()

    def is_valid_floor(self, floor):
        microchips = [el for el in floor if el[-1] == 'm']
        generators = [el for el in floor if el[-1] == 'g']
        if len(microchips) == 0 or len(generators) == 0:
            return True

        for chip in microchips:
            if chip[:-1] + 'g' not in generators:
                return False
        return True

    def is_done(self):
        return len(self.floor_plan[3]) == self.end_amt

    def __str__(self):
        result = ''
        for i in range(len(self.floor_plan)):
            elevator = '*' if (3-i) == self.elevator_floor else ' '
            result += 'Floor ' + (str(4 - i)) + ': ' + elevator + ' ' + str(self.floor_plan[-1 - i]) + '\n'
        return result

game1 = Game(floors1, 0, 0, game1amt)
game1.process_turn()

# game2 = Game(floors2, 0, 0, game2amt)
# game2.process_turn()


