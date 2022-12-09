import sys
import utils.inputReaders as ir
import utils.locationHelpers as lh

print("Day 9: Rope Bridge")

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#read file
motion_head = ir.read_oneline_records_as_list_entries(puzzle_file)

def is_adjacent(tail_pos,head_pos):
    adj = False
    distance = lh.get_manhattan_dist(tail_pos,head_pos)
    if tail_pos[0] == head_pos[0] or tail_pos[1]==head_pos[1]:
        if distance <=1:
            adj =True
    elif distance == 2:
            adj = True
    return adj

def move_tail(from_pos,head_pos):
    new_pos = [from_pos[0],from_pos[1]]
    vect_x = head_pos[0] - from_pos [0]
    vect_y = head_pos[1] - from_pos [1]
    if not is_adjacent  (from_pos, head_pos ):
        # the same row
        if vect_y == 0:
            new_pos[0] = from_pos [0] + int(vect_x/2)
        # the same col
        elif vect_x == 0:
            new_pos[1] = from_pos [1] + int(vect_y/2)
        # diagonal
        elif abs(vect_x) > abs(vect_y):
            new_pos [0] = from_pos [0] + int(vect_x/2)
            new_pos [1] = from_pos [1] + vect_y
        elif abs(vect_x) < abs(vect_y):
            new_pos [0] = from_pos [0] + vect_x
            new_pos [1] = from_pos [1] + int(vect_y/2)
        else:
            new_pos [0] = from_pos [0] + int(vect_x/2)
            new_pos [1] = from_pos [1] + int(vect_y/2)

    return new_pos

def move_head(from_pos,direction):
    new_pos = [from_pos[0],from_pos[1]]
    if direction == "L":
        new_pos[0] = from_pos[0]-1
    elif direction  == "R":
        new_pos[0] = from_pos[0]+1
    elif direction  == "U":
        new_pos[1] = from_pos[1]+1
    elif direction == "D":
        new_pos[1] = from_pos[1]-1
    return  new_pos


tail_spots = [[0,0]]
head_pos = [0,0]
tail_pos = [0,0]
for move in motion_head:
    direction, dist  = move.split(' ')
    dist = int(dist)
    for step in range(dist):
        head_pos = move_head (head_pos, direction )
        tail_pos = move_tail (tail_pos, head_pos)
        if tail_pos not in tail_spots:
            tail_spots.append(tail_pos)

print ("Part 1: number of positions the tail visited: {}".format(len(tail_spots)))

tail_spots = [[0,0]]
head_pos = [0,0]
num_tails = 9
tail_pos = []
for i in range(num_tails):
    tail_pos.append([0,0])

for move in motion_head:
    direction, dist  = move.split(' ')
    dist = int(dist)
    for step in range(dist):
        head_pos = move_head (head_pos, direction )
        tail_pos[0] = move_tail (tail_pos[0], head_pos)
        for t in range(1,num_tails):
            tt = [tail_pos[t][0],tail_pos[t][1]]
            tail_pos[t] = move_tail (tail_pos[t], tail_pos[t-1])
        if tail_pos[8] not in tail_spots:
            tail_spots.append(tail_pos[8])

print ("Part 2: number of positions the tail visited: {}".format(len(tail_spots)))
