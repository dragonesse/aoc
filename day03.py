import sys;
import utils.inputReaders as ir

print("Day 3: Rucksack Reorganization");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#read file
backpacks = ir.read_oneline_records_as_list_entries(puzzle_file)

def get_priority (item):
    priority = 0
    if item.islower():
        priority = ord(item) - 96
    else:
        priority = ord(item) - 38
    return priority

def find_duplicates (load):
    items_per_compartment = int(len(load)/2)

    for item in load[:items_per_compartment]:
        if item in load[items_per_compartment:]:
            return item


priorities = 0
for carry in backpacks:
    priorities += get_priority( find_duplicates(carry))


print ("Part 1: the total priority is: {}".format(priorities))

priorities = 0

for team_num in range(0,len(backpacks),3):
    team_check = 0
    team_load = sorted(backpacks[team_num : team_num+3],key=len)
    for item in team_load [0] :
        if item in  team_load [1] and item in team_load [2]:
            priorities += get_priority (item)
            break

print ("Part 2: the total priority is: {}".format(priorities))
