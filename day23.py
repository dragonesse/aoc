import sys
import re
import math
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
strongest_bot = max(nanorobots,key = lambda x:x[3])
max_radius = strongest_bot[3]
# print(max_radius)

def cab_distance (spoint,epoint):
    return abs(epoint[0]-spoint[0])+abs(epoint[1]-spoint[1])+abs(epoint[2]-spoint[2])

num_in_range = 0
for i in nanorobots:
    if cab_distance(i,strongest_bot) <= max_radius:
        num_in_range +=1

print ("the number of nanobots in range of strongest signal is: %d" %(num_in_range))
