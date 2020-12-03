import sys
import re

print("Day 3 puzzle: Toboggan Trajectory");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#open file

the_map = []

# sample input: 1-11 h: hhhhchhhhjhph

with open(puzzle_file, 'r') as puzzle_in:
    for     cur_line in puzzle_in:
        the_map.append(cur_line.strip().replace(".","0").replace("#","1"))

puzzle_in.close()


area_hsize = len(the_map[0])
area_vsize = len(the_map)

def has_reach_bottom (y,forrest_y):
    if y>= forrest_y:
        return True
    else:
        print ("still sliding")
        return False

def has_reach_side (x,forrest_x):
    if x>= forrest_x:
        return True
    else:
        return False

def move_toboggan (pos,slope):
    print ("moving sled from",cur_pos)
    if has_reach_side(pos[0] + slope [0], area_hsize):
        print ("wrap up")
        pos [0] =  (pos[0] + slope [0])-(area_hsize)
    else:
        pos [0] += slope[0]
    pos [1] += slope [1]

trees_counter = 0
cur_pos = [0,0]


slope = [3,1]

while not has_reach_bottom (cur_pos[1],area_vsize):
    trees_counter += int(the_map[cur_pos[1]][cur_pos[0]])
    move_toboggan(cur_pos,slope)


print ("Number of hit trees #1: %d" %trees_counter)
