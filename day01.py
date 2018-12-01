import re;
import sys;

print("Day 1 puzzle: Chronal Calibration");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];


#open file
drift_steps = []

with open(puzzle_file, 'r') as puzzle_in:
    for cur_line in puzzle_in:
        drift_steps = [int(line) for line in puzzle_in]
puzzle_in.close()

print (drift_steps)

# calculate the total drift
drift_sum = sum (drift_steps)

print ("The total drift is: %d" %(drift_sum));