import sys
import utils.inputReaders as ir
import utils.locationHelpers as lh
print("Day 12: Rain Risk");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

directions = ir.read_oneline_records_as_list_entries(puzzle_file)




def move_north (amount, cur_pos):
    return  [cur_pos[0], cur_pos [1] + amount]

def move_south (amount, cur_pos):
    return  [cur_pos[0], cur_pos [1] - amount]

def move_east (amount, cur_pos):
    return  [cur_pos[0] + amount, cur_pos [1]]

def move_west (amount, cur_pos):
    return  [cur_pos[0] - amount, cur_pos [1]]

def move_forward (amount, cur_pos,cur_dir):
    return movements[cur_dir](amount,cur_pos)

def turn_right (amount, cur_dir):
    # next_left = ["N","W","S","E"]
    next_right=["S","W","N","E"]
    index_now = next_right.index(cur_dir)
    # init_pos, dist, size
    index_next = lh.move_one_dimension_wrapped(index_now,int(amount/90),4)
    return next_right[index_next]

def turn_left (amount, cur_dir):
    next_left = ["N","W","S","E"]
    index_now = next_left.index(cur_dir)
    index_next = lh.move_one_dimension_wrapped(index_now,int(amount/90),4)
    return next_left[index_next]

movements ={
    "N": move_north,
    "S": move_south,
    "R": turn_right,
    "L": turn_left,
    "F": move_forward,
    "E": move_east,
    "W": move_west
}
def move(direction, amount, cur_pos, cur_dir):
    if direction == "N":
        cur_pos = move_north (amount,cur_pos)
    if direction == "S":
        cur_pos = move_south (amount,cur_pos)
    if direction == "E":
        cur_pos = move_east (amount,cur_pos)
    if direction == "W":
        cur_pos = move_west (amount,cur_pos)
    if direction == "F":
        cur_pos = move_forward(amount,cur_pos,cur_dir)
    if direction == "R":
        cur_dir = turn_right (amount, cur_dir)
    if direction == "L":
        cur_dir = turn_left (amount, cur_dir)

    return [cur_pos,cur_dir]

cur_pos = [0,0]
cur_dir = "E"

for mv in directions:
    move_type = mv[0]
    move_dist = int(mv[1:])
    [cur_pos,cur_dir] = move(move_type,move_dist,cur_pos,cur_dir)

print ("The final position is: ", cur_pos)
print ("The distance is: %d" %(abs(cur_pos[0])+abs(cur_pos[1])))
