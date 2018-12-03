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
        papavero_forms.append( cut_id[1:6])

puzzle_in.close()

# print (papavero_forms)

fabric = {}
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

non_overlap_candidate = ""
non_overlap_sheet = []
for [claim_id,left,top,w,h] in papavero_forms:
    # print ("processing piece ", [left,top,w,h])
    sheet = occupied_space(left,top,w,h)
    # print ("checking overlaps")
    for patch in sheet:
        overlap = False
        if patch not in fabric:
            # print ("adding %s to fabric inventory" %(patch))
            fabric[patch] = 1
        else:
            # print("found an overlap on %s" %(sheet))
            overlap = True
            fabric[patch] = fabric[patch] + 1
            # check as well if we did not hit the potentially non-overlapping piece
            if patch in non_overlap_sheet:
                non_overlap_candidate = ""
                non_overlap_sheet = []
    if not overlap:
        non_overlap_candidate = claim_id
        non_overlap_sheet = sheet

# we suppose to have by now a dictionary, with key as piece of fabric and value,
# how frequently it is refernced. To find a number of overlapping inches
# from the size of patches, substract the ones with single reference
single_use = 0
# for i in fabric.values():
#     if i == 1:
#         single_use += 1

single_use = Counter(fabric.values()).most_common()[0][1]
print (single_use)

overlap_size = len(fabric) - single_use

print ("The size of overlap is %d inches" %(overlap_size))
print ("The non-ovelaping piece is %s" %(non_overlap_candidate))