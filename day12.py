import sys
import re

print("Day 12 puzzle: Subterranean Sustainability");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#open file
init_state = [0,0]
game_of_life = {}

with open(puzzle_file, 'r') as puzzle_in:
    init_state = list(puzzle_in.readline().strip("\n").split(": ")[1])

    puzzle_in.readline()

    for cur_line in puzzle_in:
        [key,val] = cur_line.strip("\n").split(" => ")
        game_of_life[key] = val
puzzle_in.close()

def get_LLCRR_key (pot_num, state):
    return ''.join(state[pot_num:pot_num+5])

def get_plant_next_state (cur_state,algo):
    return algo[cur_state] if cur_state in algo.keys() else "."

def set_plant_next_state (pot_num, state, next_gen):
    next_gen[pot_num+2] = state
    return

def set_rear_buffer(state,unconditional=False):
    if state[-4:].count("#")>0 or unconditional:
        [state.append(".") for x in range(4)]
        return True
    else:
        return False

def set_front_buffer(state, unconditional=False):
    if state[:4].count("#")>0 or unconditional:
        [state.insert(0,".") for x in range(4)]
        return True
    else:
        return False

# add a buffer in front and rear of the row
set_rear_buffer(init_state)
set_front_buffer(init_state)

print (''.join(init_state))

def compare_with_pattern (pattern,state,offset):
    return ( pattern in ''.join(state))

num_gen = 20
next_state = ["."]*len(init_state)

pot_offs = 4
# after some time, the pattern repats and just moves one position right for each generation
# pattern = "#.#.....#.#.....#.#.........#.#.....#.#..........#.#.....#.#....#.#........#.#......#.#"
pattern = "#.##.##.##..##.##.##.##.##.##.##.##..##.##.#....................#.##.##.##.#..##.##..##.##.##.##.##.##.#.......#.##.##.#...................#.##.##.##.##.##.##.##.#.......#.##.##.#"
# for ng in range(num_gen):
ng = 0
while True:
    num_pots = len(init_state)
    for pn in range (num_pots-2):

        if ng%2 == 0:
            pk= get_LLCRR_key(pn,init_state)
            set_plant_next_state(pn,get_plant_next_state(pk,game_of_life),next_state)
        else:
            pk= get_LLCRR_key(pn,next_state)
            set_plant_next_state(pn,get_plant_next_state(pk,game_of_life),init_state)

    if ng%2 == 0:
        print (''.join(next_state))
        if compare_with_pattern(pattern,next_state,pot_offs):
            print ("After %d generations, pattern appears" %(ng))
            print(''.join(pattern))
            print(''.join(next_state))
            break
        if set_rear_buffer(next_state):
            set_rear_buffer(init_state,True)
        if set_front_buffer(next_state):
            set_front_buffer(init_state,True)
            pot_offs += 4

    else:
        print (''.join(init_state))
        if compare_with_pattern(pattern,init_state,pot_offs):
            print ("After %d generations, pattern appears" %(ng))
            print(''.join(pattern))
            print(''.join(next_state))
            break

        if set_rear_buffer(init_state):
            set_rear_buffer(next_state, True)
        if set_front_buffer(init_state):
            set_front_buffer(next_state, True)
            pot_offs += 4
    ng += 1

# calculate the sum
num_gen = 50000000000
total = 0

for i in range(len(init_state)):
    if init_state[i] =="#":
        # print ("pot index: %d" %(i-pot_offs))

        total += (i - pot_offs) + (num_gen - ng + 1)

print ("The total after %d generations is: %d" %(num_gen,total))

