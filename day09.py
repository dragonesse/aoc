import re;
import sys;

print("Day 9 puzzle: Stream Processing");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

stream = "";

#open file
with open(puzzle_file, 'r') as puzzle_in:
    stream = puzzle_in.read();

puzzle_in.close();

group_lev = 0;
grp_id  = {};
score = 0;

in_garbage_bin = 0;

# analyse stream and count groups
i = 0;
num_garbarge = 0;
while i < len(stream):

    if stream [i] == '!':
        # ignore the next character
        i += 2;
        continue;

    if stream [i] == '<':
        in_garbage_bin = True;

    if stream [i] == '>':
        in_garbage_bin = False;
        # we counted starting <, so need to remove it
        num_garbarge -= 1;

    if not in_garbage_bin:
        if stream [i] == '{':
            group_lev += 1;
            if group_lev not in grp_id:
                grp_id[group_lev] = 0;

        if stream [i] == '}':
            grp_id[group_lev] += 1;
            group_lev -= 1;
    # we want to count total garbage chars as well
    else:
        num_garbarge += 1;

    i += 1;

score = 0;
for key in grp_id.keys():
    score += int(key) * int(grp_id[key]);

print ("total num of groups: %d" %( sum( grp_id.values() )) );
print ("total num of removed garbage: %d" %(num_garbarge) );
print ("total score is: %d" %(score) );