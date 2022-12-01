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

supply_list = []
for elf_inventory in food:
    supply_list.append(sum(int(cal) for cal in elf_inventory))

print ("Part 1: the most available calories is: {}".format(max(supply_list)))

top3 = sorted(supply_list)[-3:]
print ("Part 2: the sum of calories for top 3 equipped elves is: {}".format(sum(top3)))
