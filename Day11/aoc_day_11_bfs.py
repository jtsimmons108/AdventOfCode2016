from __future__ import print_function
import itertools
from collections import deque




floors1 = [['pog', 'thg', 'thm', 'prg', 'rug', 'rum', 'cog', 'com'], ['pom', 'prm'], [], []]
# Floor starting point for 2nd part
floors2 = [['pog', 'thg', 'thm', 'prg', 'rug', 'rum', 'cog', 'com', 'elm', 'elg', 'dim', 'dig'], ['pom', 'prm'],[],[]]
moves = []


class Game(object):
    def __init__(self, floor_plan, moves, elevator_floor):
        self.floor_plan = [floor[::] for floor in floor_plan]
        self.moves = moves
        self.elevator_floor = elevator_floor

    '''
        Make sure the floor states are the same for every floor in both games
    '''

    def has_same_game_state(self, other):
        for i in range(len(self.floor_plan)):
            if self.get_floor_state(i) != other.get_floor_state(i):
                return False
        return True

    def get_game_state(self):
        return [self.get_floor_state(i) for i in range(len(self.floor_plan))] + [(self.elevator_floor,)]

    '''
        Count the number of individual generators, individual microchips, and pairs on the floor
    '''
    def get_floor_state(self, floor_number):
        elements = sorted(self.floor_plan[floor_number])
        i = 0
        gens, chips, pairs = 0, 0, 0
        while i < len(elements):
            if elements[i][-1] == 'g' and i < len(elements) - 1 and elements[i + 1][:-1] == elements[i][:-1]:
                pairs += 1
                i += 2
            else:
                if elements[i][-1] == 'g':
                    gens += 1
                else:
                    chips += 1
                i += 1
        return gens, chips, pairs

    '''
        Make sure the pair to move are either the same type, both generators, or both microchips
    '''
    def is_valid_pair(self, pair):
        el1, el2 = pair
        if el1[-1] == el2[-1] or el1[:-1] == el2[:-1]:
            return True
        return False

    '''
        If there are no generators or no microchips, it's a valid floor.
        Otherwise, make sure the chip has its pair on the floor
    '''
    def is_valid_floor(self, floor):
        microchips = [el for el in floor if el[-1] == 'm']
        generators = [el for el in floor if el[-1] == 'g']
        if len(microchips) == 0 or len(generators) == 0:
            return True

        for chip in microchips:
            if chip[:-1] + 'g' not in generators:
                return False
        return True

    '''
        Find all valid pairs that can be moved up, sorted before return so it tries to move generators up before
        pairs of only microchips
    '''
    def get_pairs_to_move_up(self):
        if self.elevator_floor == 3:
            return []
        pairs = []
        for pair in itertools.combinations(self.floor_plan[self.elevator_floor], 2):
            if self.is_valid_pair(pair) and self.can_move_pair(pair, 1):
                pairs.append(pair)
        return sorted(pairs, key=lambda x: x[0][-1])

    '''
        Don't look for elements to move down if elevator is on the bottom or if there is nothing in all the rows
        below current position
    '''
    def get_pairs_to_move_down(self):
        if self.elevator_floor == 0 or sum(len(self.floor_plan[i]) for i in range(self.elevator_floor)) == 0:
            return []
        pairs = []
        for pair in itertools.combinations(self.floor_plan[self.elevator_floor], 2):
            if self.is_valid_pair(pair) and self.can_move_pair(pair, -1):
                pairs.append(pair)
        return pairs

    '''
        Make sure the new floor and old floor will be valid with the move
    '''
    def can_move_pair(self, pair, direction):
        return self.is_valid_floor([el for el in self.floor_plan[self.elevator_floor] if el not in pair]) \
               and self.is_valid_floor(self.floor_plan[self.elevator_floor + direction] + list(pair))

    def can_move_one(self, element, direction):
        return self.is_valid_floor([el for el in self.floor_plan[self.elevator_floor] if el != element]) \
               and self.is_valid_floor(self.floor_plan[self.elevator_floor + direction] + [element])

    def get_elements_to_move_down(self):
        if self.elevator_floor == 0 or sum(len(self.floor_plan[i]) for i in range(self.elevator_floor)) == 0:
            return []

        elements = []
        for el in self.floor_plan[self.elevator_floor]:
            if self.can_move_one(el, -1):
                elements.append((el,))
        return elements


    def get_elements_to_move_up(self):
        if self.elevator_floor == 3:
            return []
        elements = []
        for el in self.floor_plan[self.elevator_floor]:
            if self.can_move_one(el, 1):
                elements += [(el,)]
        return elements

    def get_items_to_move_up(self):
        return self.get_elements_to_move_up() + self.get_pairs_to_move_up()

    def get_items_to_move_down(self):
        return self.get_elements_to_move_down() + self.get_pairs_to_move_down()

    '''
        Move all of the items to the move floor and remove them from the old floor.
        Increment moves and move the elevator
    '''
    def move(self, items, direction):
        for item in items:
            self.floor_plan[self.elevator_floor].remove(item)
            self.floor_plan[self.elevator_floor + direction].append(item)
        self.elevator_floor = self.elevator_floor + direction
        self.moves += 1



    '''
        Gather all of the possible moves.  Start up a new game for each possibility
    '''

    def is_done(self):
        return len(self.floor_plan[3]) == sum([len(floor) for floor in self.floor_plan])

    def __str__(self):
        result = ''
        for i in range(len(self.floor_plan)):
            elevator = '*' if (3 - i) == self.elevator_floor else ' '
            result += 'Floor ' + (str(4 - i)) + ': ' + elevator + ' ' + str(self.floor_plan[-1 - i]) + '\n'
        return result

for floors in [floors1, floors2]:
    game = Game(floors, 0, 0)
    views = 0
    states = []
    nodes = deque()
    nodes.append(game)
    states.append(game.get_game_state())

    while len(nodes) > 0:
        curr_game = nodes.popleft()
        views += 1
        if curr_game.is_done():
            print(curr_game.moves)
            print(views)
            break
        for items in curr_game.get_items_to_move_up():
            new_game = Game(curr_game.floor_plan, curr_game.moves, curr_game.elevator_floor)
            new_game.move(items, 1)
            if new_game.get_game_state() not in states:
                states.append(new_game.get_game_state())
                nodes.append(new_game)
        for items in curr_game.get_items_to_move_down():
            new_game = Game(curr_game.floor_plan, curr_game.moves, curr_game.elevator_floor)
            new_game.move(items, -1)
            if new_game.get_game_state() not in states:
                states.append(new_game.get_game_state())
                nodes.append(new_game)