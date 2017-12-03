import re;
import sys;

print("Day 2 puzzle: Corruption checksum");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];


#open file
checksum = 0;
with open(puzzle_file, 'r') as puzzle_in:
    for cur_line in puzzle_in:
        sheet_line = [];
        sheet_line = [int(x) for x in cur_line.strip("\n").split()];
        # sheet_line = cur_line.strip("\n").split();
        print (sheet_line);
        checksum += max(sheet_line) - min(sheet_line);
puzzle_in.close();
print ("checksum is %d" %(checksum));

