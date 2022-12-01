import sys;
import utils.inputReaders as ir

print("Day 1: Calorie Counting");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#read file
food = ir.read_multiline_records_as_list_entries(puzzle_file)

#level 1 solution
num_increments = 0
supply_list = []
for elf_inventory in food:
    supply_list.append(sum(int(cal) for cal in elf_inventory))

print (supply_list)

print ("Part 1: the most available calories is: {}".format(max(supply_list)))


