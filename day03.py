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
    if item == '':
        print ("unexpected item")
    elif item.islower():
        priority = ord(item) - 96
    else:
        priority = ord(item) - 38
    print ("item {}:{}".format(item,priority))
    return priority

def find_duplicates (load):
    items_per_compartment = int(len(load)/2)
    duplicates = ''

    for item in load[:items_per_compartment]:
        if (item in load[items_per_compartment:]) and (item not in duplicates):
                duplicates = item
                break
    return duplicates


priorities = 0
for carry in backpacks:
    priorities += get_priority( find_duplicates(carry))


print ("Part 1: the total priority is: {}".format(priorities))

sys.exit(0)
score = 0
for game in secret_book:
    score += determine_game_outcome(choose_your_move(game))

print ("Part 2: your score is: {}".format(score))
