import sys
import re

print("Day 7 puzzle: The Sum of Its Parts")

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!")
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#open file
ikea_booklet = {}
split_pattern = re.compile(r'\b([A-Z]{1})\b.*\b([A-Z]{1})\b')

with open(puzzle_file, 'r') as puzzle_in:

    for cur_line in puzzle_in:
        [_, parent, child, _] = re.split(split_pattern,cur_line)
        if parent not in ikea_booklet.keys():
            ikea_booklet[parent] = child
        else:
            ikea_booklet[parent] = ikea_booklet[parent] + child

puzzle_in.close()

for i in ikea_booklet.keys():
    print ("parent %s children %s" %(i,ikea_booklet[i]))

def can_execute_step (step, instructions):
    # we can proceed with a step, if its children are on list of values only once
    print ("-----validating step %s " %(step))
    num_hits = 0
    for v in instructions.values():
       print ("checking value %s for presence of %s" %(v,step))
       if v.count(step) > 0 :
            num_hits += 1

    return num_hits == 0

# find the master parent
parent = []
for p in ikea_booklet.keys():
    if can_execute_step(p,ikea_booklet):
        parent.append(p)

print ("following steps are independent: %s" %(parent))


build_sequence = ""


print ("The order of tasks is: ", build_sequence)

