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

# sample form expected on input:
#1 @ 286,440: 19x24
split_pattern = re.compile(r'^#(\d+)\s*\@\s*(\d+),(\d+):\s*(\d+)x(\d+)$')

#open file
papavero_forms = []

with open(puzzle_file, 'r') as puzzle_in:
    for cur_line in puzzle_in:
        cut_id = re.split(split_pattern,cur_line.strip("\n"))
        papavero_forms.append( cut_id[1:6])

puzzle_in.close()

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

#id-sheet map
non_overlap_candidate = {}
for [claim_id,left,top,w,h] in papavero_forms:
    sheet = occupied_space(left,top,w,h)
    overlap = False
    cand_to_del = []
    for patch in sheet:
        if patch not in fabric:
            fabric[patch] = 1
        else:
            overlap = True
            fabric[patch] = fabric[patch] + 1
            # check potential overlap with non-overlapping (yet) pieces
            for cand_id, cand_sheet in non_overlap_candidate.items():
                if patch in cand_sheet:
                    if cand_id not in cand_to_del:
                        cand_to_del.append(cand_id)

    # can't modify dictionary inside the loop
    for cand_id in cand_to_del:
        del non_overlap_candidate[cand_id]
    if not overlap:
        non_overlap_candidate[claim_id] = sheet.copy()

# we suppose to have by now a dictionary, with key as piece of fabric and value,
# how frequently it is referenced. To find a number of overlapping inches
# from the size of patches, substract the ones with single reference

single_use = Counter(fabric.values()).most_common()[0][1]
overlap_size = len(fabric) - single_use

print ("The size of overlap is %d inches" %(overlap_size))
print ("The non-ovelaping piece is %s" %(non_overlap_candidate.keys()))