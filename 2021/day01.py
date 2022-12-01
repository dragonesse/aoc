import sys;
import utils.inputReaders as ir

print("Day 1 puzzle: Sonar Sweep");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#read file
scan_data = ir.read_int_records_as_list_entries(puzzle_file)

#level 1 solution
num_increments = 0
for i in range(1,len(scan_data)):
    if scan_data[i]>scan_data[i-1]:
        num_increments+=1

print ("Part 1: number of increments: {}".format(num_increments))

#level 2
num_increments = 0
win_size = 3
for i in range(len(scan_data)-3):
    win1 = sum(scan_data[i:i+win_size])
    win2 = sum(scan_data[i+1:i+1+win_size])
    if win2>win1:
        num_increments+=1

print ("Part 2: number of increments: {}".format(num_increments))

