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

def traverse_disc (single_disc, map_of_discs, weights_vals):
    tot_balance = int(weights_vals[single_disc]);
    if single_disc not in map_of_discs.keys():
        # disc that does not carry anything
        pass;
    else:
        for child_disc in map_of_discs[single_disc]:
            tot_balance += traverse_disc (child_disc, map_of_discs, weights_vals);
    return tot_balance;

bal_weights = {};
root = "";

# find the root of the tree
for k in weights.keys():
    found_parent = False;
    for child in maps.values():
        if k in child:
            found_parent = True;
            break;
    if not found_parent:
        print ("program %s is the root" %(k));
        root = k;
        break;

key = root;

while key:
    unbalanced = [];
    bal_weights = {};
    for disc in maps[key]:
        print ("traversing disc %s" %(disc));
        bal_weights [disc] = traverse_disc(disc,maps,weights);

        print ("balance weight of disc %s is %d" %(disc, bal_weights[disc]));
    # get the unique value in the map of balances to find odd disc
    countMap = {};
    for w in bal_weights.values():
        countMap[w] = countMap.get(w,0) + 1;
    unbalanced = [ k for k, v in bal_weights.items() if countMap[v] == 1];
    print ("unbalanced disc is: %s" %(unbalanced));
    key = ''.join(unbalanced);
