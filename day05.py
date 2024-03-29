import sys;
import utils.inputReaders as ir
import re

print("Day 5: Supply Stacks");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#read file
puzzle_in = ir.read_oneline_records_as_list_entries(puzzle_file, stripping = False)


cargo = []
moves = []

cargo_pat = re.compile(r'^\s*\[[A-Z]\]')
move_pat = re.compile(r'move ([0-9]+) from ([0-9]) to ([0-9])')
container_pat = re.compile(r'^')

for line in puzzle_in:
    if re.match(cargo_pat,line):
        cargo.append(line)
    if re.match(move_pat,line):
        moves.append(line)

def get_container (row_of_containers, stack_id):
    offset = (3 * stack_id) + (stack_id)
    return row_of_containers[offset:offset+4]

# rebuild cargo info so that each line represents a stack instead of row of containers
cargo_flip = []

num_stacks = int((len(cargo[0]) + 1) /4)
for s in range(num_stacks):
    cargo_flip.append('')

for cargo_row in cargo[::-1]:
    for stack_id in range(num_stacks):
        container = get_container(cargo_row,stack_id)
        if container.startswith('['):
            cargo_flip[stack_id] += container[1]

cargo_flip_p2 = cargo_flip.copy()

def parse_move (move, move_pat):
    return [int(grp) for grp in re.match(move_pat,move).groups()]

for move in moves:
    quantity, src, dest = parse_move (move, move_pat)
    for m in range(quantity):
        cargo_flip[dest-1] += cargo_flip[src-1][-1]
        cargo_flip[src-1] = cargo_flip[src-1][:-1]

top_containers=""
for c in cargo_flip:
    top_containers += c[-1]

print ("Part 1: top container are: {}".format(top_containers))

for move in moves:
    quantity, src, dest = parse_move (move, move_pat)
    cargo_flip_p2[dest-1] += cargo_flip_p2[src-1][quantity*(-1):]
    cargo_flip_p2[src-1] = cargo_flip_p2[src-1][:quantity*(-1)]

top_containers=""
for c in cargo_flip_p2:
    top_containers += c[-1]
print ("Part 2: top container are: {}".format(top_containers))
