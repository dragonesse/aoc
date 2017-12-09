import re;
import sys;

print("Day 7 puzzle: Recursive Circus");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];


#open file
weights = {};
maps    = {};
pattern_weight = re.compile(r'(\w+)\s+\((\d+)\)\s*(.*)');

with open(puzzle_file, 'r') as puzzle_in:
    for cur_line in puzzle_in:
        # ebii (61)
        # fwft (72) -> ktlj, cntj, xhth
        # all entries have at least disc name and it's weight
        [ prog,weight,children] = pattern_weight.match(cur_line).groups();

        if prog not in weights:
            weights[prog] = weight;

        if children is not "":
            maps[prog] = children[3:].split(", ");

puzzle_in.close();

for key in weights.keys():
    found_parent = False;
    for child in maps.values():
        if key in child:
            found_parent = True;
            break;
    if not found_parent:
        print ("program %s is the root" %(key));
        break;

