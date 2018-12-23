import sys
import re
print("Day 23 puzzle: Experimental Emergency Teleportation");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#open file
nanorobots =[]
# pos=<0,0,0>, r=4
pattern =  re.compile(r'^.*(\-*[0-9]+),(\-*[0-9]+),(\-*[0-9]+).*=([0-9]+)$')
with open(puzzle_file, 'r') as puzzle_in:
    for cur_line in puzzle_in:
        nanorobots.append( (list(int(x) for x in re.match(pattern,cur_line).group(1,2,3,4))) )

puzzle_in.close()
# print(nanorobots)
max_radius = max(nanorobots,key = lambda x:x[3])[3]
print(max_radius)