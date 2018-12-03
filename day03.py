import sys
import re
from collections import Counter

print("Day 3 puzzle: No Matter How You Slice It");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];


#open file
papavero_forms = []

# sample form expected on input
#1 @ 1,3: 4x4
#1 @ 286,440: 19x24
split_pattern = re.compile(r'^#(\d+)\s*\@\s*(\d+),(\d+):\s*(\d+)x(\d+)$')
with open(puzzle_file, 'r') as puzzle_in:
    for cur_line in puzzle_in:
        cut_id = re.split(split_pattern,cur_line.strip("\n"))
        papavero_forms.append( cut_id[2:6])

puzzle_in.close()

print (papavero_forms)

fabric = {}
overlap_size = 0
def occupied_space(offset_left, offset_top, width, length):
    patches = []
    startx = int(offset_left)
    starty = int(offset_top)
    for i in range (int(width)):
        x = startx + i
        for j in range (int(length)):
            y = starty + j
            patches.append(str(x)+"-"+str(y))

    return patches

[left,top,w,h] = papavero_forms[0]
print (occupied_space(left,top,w,h))

for [left,top,w,h] in papavero_forms:
     sheet = occupied_space(left,top,w,h)
     for patch in sheet:
        if patch not in fabric:
            fabric[patch] = 1
        else:
            print("found an overlap")
            overlap_size += 1

print ("The size of overlap is %d inches" %(overlap_size))
