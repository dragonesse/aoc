import sys
import utils.inputReaders as ir
import re

print("Day 8: Treetop Tree House");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#read file
the_wood = ir.read_oneline_records_as_list_entries(puzzle_file)

for i in range(len(the_wood)):
    the_wood[i] = [int(w) for w in list(the_wood[i])]


def is_visible(x,y,wood):
    visible = False
    wood_l = len(wood[0])
    wood_h = len(wood)
    tree_h = wood[x][y]
    if (x in [0, wood_l]) or (y in [0, wood_h]):
        visible = True
    else:
        num_blindspots = 0
        # tree is visible if can be seen from any side
        for i in range(0,x):
            if wood[i][y] >= tree_h:
                num_blindspots += 1
                break
        for i in range(x+1,wood_l):
            if wood[i][y] >= tree_h:
                num_blindspots += 1
                break
        for j in range(0,y):
            if wood[x][j] >= tree_h:
                num_blindspots += 1
                break
        for j in range(y+1,wood_h):
            if wood[x][j] >= tree_h:
                num_blindspots += 1
                break
        visible = True if num_blindspots < 4 else False
    return visible

def get_view_score(x,y,wood):
    score = 0
    wood_l = len(wood[0])
    wood_h = len(wood)
    tree_h = wood[x][y]
    if (x in [0, wood_l]) or (y in [0, wood_h]):
        score = 0
    else:
        num_spots = [0,0,0,0]
        # check left
        i = x - 1
        while i >= 0:
            num_spots[0] += 1
            if wood[i][y] >= tree_h:
                break
            else:
                i -= 1
        # check right
        i = x + 1
        while i < wood_l:
            num_spots[1] += 1
            if wood[i][y] >= tree_h:
                break
            else:
                i += 1
        # check up
        j = y - 1
        while j >=0 :
            num_spots[2] += 1
            if wood[x][j] >= tree_h:
                break
            else:
                j -= 1
        # check down
        j = y + 1
        while j < wood_h:
            num_spots[3] += 1
            if wood[x][j] >= tree_h:
                break
            else:
                j += 1
        score = num_spots[0]*num_spots[1]*num_spots[2]*num_spots[3]

    return score

num_visible = 0
row = 0
col = 0

for row in range (len(the_wood)):
    for col in range (len(the_wood[0])):
        if is_visible(row,col,the_wood):
            num_visible += 1

print ("Part 1: number visible trees is: {}".format(num_visible))

visibility_score = 0
row = 0
col = 0

for row in range (len(the_wood)):
    for col in range (len(the_wood[0])):
        tree_score = get_view_score(row,col,the_wood)
        if tree_score > visibility_score:
            visibility_score = tree_score


print ("Part 2: the biggest visibility score is: {}".format(visibility_score))

