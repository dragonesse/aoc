import sys;
import math;
print("Day 3 puzzle: Spiral Memory");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#open file
with open(puzzle_file, 'r') as puzzle_in:
    for cur_line in puzzle_in:
        mem_cell = int(cur_line.strip("\n"));
puzzle_in.close();

distance = 0;
spiral_len = 1;
spiral_layer = 0;
spiral_side = 1;

while spiral_len < mem_cell:
    spiral_layer += 1;
    spiral_len += 4 * (spiral_side + 1);
    spiral_side += 2;

# now we need to calculate, the position on a given layer
# the layer starts in bottom-right corner and continues up, counterclockwise
rollback = spiral_len;
# the cell is somewhere in between...
# we know the maximal position on this kayer
# as well as side length
for i in range(4):
    # process cell located on side
    if rollback - mem_cell <= spiral_side - 2:
        # when calculating distance, no matter which side we are at,
        # we need to move to the level of layer "0" and then move
        # straight through all layers
        # level of layer "0" is always in the middle of side
        distance = math.fabs(mem_cell - (rollback - spiral_layer)) + spiral_layer
        break;
    rollback -= (spiral_side - 2) ;

    # process the corner
    if rollback - 1 == mem_cell:
        distance = 2 * spiral_layer;
        break;
    rollback -= 1;

print ("The distance between %d and 1 is %d" %(mem_cell,distance));

# part two - write to the cell sum of neighbours
# 147  142  133  122   59
# 304    5    4    2   57
# 330   10    1    1   54
# 351   11   23   25   26
# 362  747  806--->   ...

prev_layer_vals = {};
cur_layer_vals = {};
new_val = 1;

prev_val = 1;

spiral_side  = 1;

def calc_prev_corner(side):
    if side:
        return (side - 1)
    else:
        return 3;

def calc_next_corner(side):
    return side;

def calc_spiral_key (side,index,corner):
    return "s"+str(side)+"i"+str(index)+"c"+str(corner)

# [side, index in side, corner]
cell_pos = {
    "side":-1,
    "index":-1,
    "corner":-1
    };
while new_val < mem_cell:

    # calculate memory position
    # 17  16  15  14  13
    # 18   5   4   3  12
    # 19   6   1   2  11
    # 20   7   8   9  10
    # 21  22  23---> ...

    if cell_pos["index"] + 1 == spiral_side:
        # we need to move to corner
        cell_pos["corner"] = cell_pos["side"]
        cell_pos["side"] = -1
        cell_pos["index"] = -1
    elif cell_pos ["corner"] == 3:
        # move to next layer
        spiral_side += 2
        prev_layer_vals = cur_layer_vals.copy()
        cell_pos ["side"] = 0
        cell_pos["index"] = 0
        cell_pos ["corner"] = -1
    elif cell_pos["side"] == -1:
        # move from corner to next side
        cell_pos ["side"] = cell_pos["corner"] + 1
        cell_pos["index"] = 0
        cell_pos ["corner"] = -1
    else:
        cell_pos["index"] += 1;

    new_val = 0;

    # determine your neighbours and calculate value stored in current memory cell:
    # 147  142  133  122   59
    # 304    5    4    2   57
    # 330   10    1    1   54
    # 351   11   23   25   26
    # 362  747  806--->   ...

    # a starting cell on layer has 2 neighbours: corner from prev layer and zero index from prev layer
    if cell_pos["index"] == 0 and cell_pos["side"] == 0:
        # build a key for the layer - 1 table
        if calc_spiral_key(-1,-1,3) in prev_layer_vals:
            new_val = prev_layer_vals[calc_spiral_key(-1,-1,3)] + prev_layer_vals[calc_spiral_key(0,0,-1)]
        else:
            # this must be a first layer
            new_val = 1;

    # a corner cell has 2 neighbours: corner from prev layer and prev value from current layer
    elif cell_pos["index"] == -1:
        if calc_spiral_key(-1,-1,cell_pos["corner"]) in prev_layer_vals:
            new_val = prev_layer_vals[calc_spiral_key(-1,-1,cell_pos["corner"])] + prev_val;
        else:
            # this must be a first layer
            new_val = 1 + prev_val

    # a cell on side has up to 4 neighbours: prev value from current layer; from previous layer, we consider
    # cells indexed by: (index - 1), (index - 2), (index) amongst which some may turn out to be corners
    else:
        # we always have as neighbour the previous cell from current layer
        new_val = prev_val;

        # checking previous layer for cell accessed by (index -1) - this is a cell on the same level
        # as the one for which we calculate the sum
        if calc_spiral_key(cell_pos["side"],cell_pos["index"] - 1,-1) in prev_layer_vals:
            new_val += prev_layer_vals[calc_spiral_key(cell_pos["side"],cell_pos["index"] - 1,-1)]
        # but we might get the corner, instead
        elif (cell_pos["index"] > 0) and calc_spiral_key(-1, - 1,cell_pos["side"]) in prev_layer_vals:
            new_val += prev_layer_vals[calc_spiral_key(-1, - 1,cell_pos["side"])]
        elif (cell_pos["index"] == 0) and calc_spiral_key(-1, - 1,calc_prev_corner(cell_pos["side"])) in prev_layer_vals:
            new_val += prev_layer_vals[calc_spiral_key(-1, - 1,calc_prev_corner(cell_pos["side"]))]

        # checking previous layer for cell accessed by (index)
        if calc_spiral_key(cell_pos["side"],cell_pos["index"] , -1) in prev_layer_vals:
            new_val += prev_layer_vals[calc_spiral_key(cell_pos["side"],cell_pos["index"], -1)]
        # but we might consider the corner instead, if we are not the last cell on a side
        # the last cell does not have (index) neighbour in the previous layer
        elif (cell_pos["index"] != spiral_side -1) and calc_spiral_key(-1,-1,calc_next_corner(cell_pos["side"])) in prev_layer_vals:
            new_val += prev_layer_vals[calc_spiral_key(-1,-1,calc_next_corner(cell_pos["side"]))]

        # checking previous layer for cell accessed by (index - 2)
        if calc_spiral_key(cell_pos["side"],cell_pos["index"] - 2, -1) in prev_layer_vals:
            new_val += prev_layer_vals[calc_spiral_key(cell_pos["side"],cell_pos["index"] - 2, -1)]
        # but we might hit a corner, if we are not a first cell. The first cell does not have
        # (index - 2) neighbour, it has instead a neighbour from current layer
        elif (cell_pos["index"] > 0) and calc_spiral_key(-1,-1,calc_prev_corner(cell_pos["side"])) in prev_layer_vals:
            new_val += prev_layer_vals[calc_spiral_key(-1,-1,calc_prev_corner(cell_pos["side"]))]

        # if no keys are stored, we are processing the first layer
        if not(len(prev_layer_vals.keys())):
            new_val += 1

        # first cell on a side (except first cell in layer), has also as a neighbour the last cell on a previous side)
        if cell_pos["index"] == 0:
            new_val += cur_layer_vals[calc_spiral_key(cell_pos["side"] -1,spiral_side - 1,-1)]

    # the last two cells on third side, has also a cell "0" as neighbour
    if (cell_pos["side"] == 3 and cell_pos["index"] == spiral_side - 1) or (cell_pos["corner"] == 3):
        new_val += cur_layer_vals[calc_spiral_key(0,0,-1)]

    # store for next loop
    cur_layer_vals[calc_spiral_key(cell_pos["side"],cell_pos["index"],cell_pos["corner"])] = new_val;
    prev_val = new_val;

print ("The value for first cell with num higher than %d is %d" %(mem_cell, new_val))