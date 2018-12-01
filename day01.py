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
    drift_steps = [int(cur_line) for cur_line in puzzle_in]
puzzle_in.close()

# calculate the total drift
drift_sum = sum (drift_steps)
print ("The total drift is: %d" %(drift_sum))

# examine for the appearance of the duplicated result
drift_res = [0]
cur_drift = 0
first_dup = False

while not first_dup:
    for delta in drift_steps:
        cur_drift += delta
        if cur_drift not in drift_res:
            drift_res.append(cur_drift)
        else:
            print ("The first duplicated frequency is: %d" %(cur_drift))
            first_dup = True
            break

