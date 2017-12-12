import math;
import sys;

print("Day 11 puzzle: Hex Ed");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

trail = "";

#open file
with open(puzzle_file, 'r') as puzzle_in:
    trail = puzzle_in.read().strip("\n").split(",");

puzzle_in.close();


def go_ne (start_x, start_y):
    return [start_x + 1,start_y + 1];

def go_nw (start_x, start_y):
    return [start_x - 1,start_y + 1];

def go_se (start_x, start_y):
    return [start_x + 1,start_y - 1];

def go_sw (start_x, start_y):
    return [start_x - 1,start_y - 1];

def go_s (start_x, start_y):
    return [start_x, start_y - 2];

def go_n (start_x, start_y):
    return [start_x, start_y + 2];

def calc_dist (x,y):
    distance = 0;
    # assume, we started at 0,0
    # the distance is the sum of movements toward the initial column and the initial row
    # to move to initial column, we need to substract y positions
    distance = math.fabs(x);
    y = math.fabs(y) - distance;

    # to move to initial row, we need to substract y positions and divide by 2
    distance = distance + math.fabs(y//2);
    return distance;

track_map = {
    "ne" : go_ne,
    "se" : go_se,
    "nw" : go_nw,
    "sw" : go_sw,
    "s"  : go_s,
    "n"  : go_n
};

# analyse stream and track current child position
start_x, start_y = 0, 0;
max_dist = 0;
for step in trail:

    [start_x, start_y] = track_map[step](start_x, start_y);
    cur_dist =  calc_dist(start_x, start_y);
    if cur_dist > max_dist:
        max_dist = cur_dist;

print ("final position is %d, %d" %(start_x,start_y));

print ("total distance is: %d" %( calc_dist(start_x, start_y)) );
print ("max distance is: %d" %( max_dist) );
