from __future__ import print_function
import itertools


start_file = open('./aoc_day_11_input.txt')
instructions = start_file.read().strip().splitlines()

# Example
# floors1 = [['hym', 'lim'], ['hyg'], ['lig'], []]


floors1 = [['pog', 'thg', 'thm', 'prg', 'rug', 'rum', 'cog', 'com'], ['pom', 'prm'], [], []]

# Floor starting point for 2nd part
# floors2 = [['pog', 'thg', 'thm', 'prg', 'rug', 'rum', 'cog', 'com', 'elm', 'elg', 'dim', 'dig'], ['pom', 'prm'],[],[]]


class Game(object):
    def __init__(self, floor_plan, moves, elevator_floor, seen_floor_states):
        self.floor_plan = floor_plan
        self.moves = moves
        self.elevator_floor = elevator_floor
        self.seen_floor_states = seen_floor_states

    '''
        Make sure the floor states are the same for every floor in both games
    '''

    def has_same_game_state(self, other):
        for i in range(len(self.floor_plan)):
            if self.get_floor_state(i) != other.get_floor_state(i):
                return False
        return True

    def get_game_state(self):
        return [self.get_floor_state(i) for i in range(len(self.floor_plan))]

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
        Make sure the pair to move is either the same type, both generators, or both microchips
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
                elements += [el]
        return elements


    def get_elements_to_move_up(self):
        if self.elevator_floor == 3:
            return []
        elements = []
        for el in self.floor_plan[self.elevator_floor]:
            if self.can_move_one(el, 1):
                elements += [el]
        return elements

    '''
        Move all of the items to the move floor and remove them from the old floor.
        Increment moves and move the elevator
    '''
    def move(self, items, new_floor):
        for item in items:
            self.floor_plan[self.elevator_floor].remove(item)
            self.floor_plan[new_floor].append(item)
        self.elevator_floor = new_floor
        self.moves += 1

    '''
        Start a new game with copies of the old information, moves the items to be moved.
        Add itself to the already seen floor states
        If the new floor state has not been seen before, go ahead and process turns from there
        I'm not sure this is working properly
    '''
    def start_new_games(self, items_to_move, direction):
        self.seen_floor_states.append(self)
        new_game = Game([floor[::] for floor in self.floor_plan], self.moves, self.elevator_floor, self.seen_floor_states)
        new_game.move(items_to_move, self.elevator_floor + direction)
        print(new_game)
        if not any(new_game.has_same_game_state(game) for game in self.seen_floor_states):
            new_game.process_turn()

    '''
        Gather all of the possible moves.  Start up a new game for each possibility
    '''
    def process_turn(self):
        if self.is_done():
            print(self.moves)
            exit()
        else:
            pairs_up = self.get_pairs_to_move_up()
            els_up = self.get_elements_to_move_up()
            pairs_down = self.get_pairs_to_move_down()
            els_down = self.get_elements_to_move_down()
            if len(pairs_up) > 0:
                for pair in pairs_up:
                    self.start_new_games(pair, 1)

            if len(els_down) > 0:
                for el in els_down:
                    self.start_new_games((el,), -1)
            if len(els_up) > 0:
                for el in els_up:
                    self.start_new_games((el,), 1)

            '''
                Moving Pairs down seems to make the parts run forever
                However, can't solve other inputs without doing this
            '''
            # if len(pairs_down) > 0:
            #     for pair in pairs_down:
            #         self.start_new_games(pair, -1)

    def is_done(self):
        return len(self.floor_plan[3]) == sum([len(floor) for floor in self.floor_plan])

    def __str__(self):
        result = ''
        for i in range(len(self.floor_plan)):
            elevator = '*' if (3 - i) == self.elevator_floor else ' '
            result += 'Floor ' + (str(4 - i)) + ': ' + elevator + ' ' + str(self.floor_plan[-1 - i]) + '\n'
        return result


game1 = Game(floors1, 0, 0, [])
game1.process_turn()

# game2 = Game(floors2, 0, 0, [])
# game2.process_turn()



