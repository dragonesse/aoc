import re;
import sys;

print("Day 6 puzzle: Memory reallocation");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

def checksum (cur_state):
    checksum = 0;
    for i in range (len(cur_state)):
        checksum += cur_state[i];
    return checksum;

def max_block (block):

    # find highest lad value
    h_load = max (block);

    # look for duplicates
    block_id = block.index(h_load);

    return block_id;

def ralloc (block_id, cur_state):
    new_state = list(cur_state);

    next_block = -1;
    if block_id == (len(cur_state) - 1):
        next_block = 0;
    else:
        next_block = block_id + 1;

    # reallocation
    num_to_realloc = cur_state[block_id];
    new_state [block_id] = 0;

    # how many full cycles will fit?
    full_cycles = -1;

    if num_to_realloc >= len (cur_state):
        full_cycles = num_to_realloc // len(cur_state);

        new_state = [x + full_cycles for x in cur_state];
        new_state[block_id] = full_cycles;
        num_to_realloc -= full_cycles * len(cur_state);

    if num_to_realloc > 0:
        for i in range(next_block,len(cur_state)):
            new_state[i] += 1;
            num_to_realloc -= 1;
            if num_to_realloc == 0:
                # nothing left for reallocation
                break;

    # if we still have something on stack, it means
    # we wrapped around the buffer
    if num_to_realloc > 0:
        for i in range (num_to_realloc):
            new_state[i] += 1;
    return new_state;

def state_fingerprint (cur_state):
    fingerprint = ' '.join(str(mem_state) for mem_state in cur_state);
    return fingerprint;

#open file
cur_state = [];
with open(puzzle_file, 'r') as puzzle_in:

    for cur_line in puzzle_in:
        cur_state = [int(x) for x in cur_line.split()];

puzzle_in.close();

states_vistited = set(); #set
states_vistited.add(state_fingerprint(cur_state));

while True:
    cs_init = checksum(cur_state);
    block_id = max_block (cur_state);

    cur_state = ralloc (block_id, cur_state);

    if checksum(cur_state) != cs_init:
        print ("REALLOCATION ERROR in %d cycle" %(len(states_vistited)));
        break;

    fingerprint = state_fingerprint(cur_state);

    if fingerprint not in states_vistited:
        states_vistited.add(fingerprint);
    else:
        print ("already was there");
        break;

cycle_id = 0;
init_state = list(cur_state);

while True:
    block_id = max_block (cur_state);
    cur_state = ralloc (block_id, cur_state);
    cycle_id += 1;

    if cur_state == init_state:
        print ("observing state again");
        break;

print ("Number of reallocation cycles for first repetition: %d" %(len(states_vistited)));
print ("Number of reallocation cycles to see first repetition again: %d" %(cycle_id));