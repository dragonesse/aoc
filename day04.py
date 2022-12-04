import sys;
import utils.inputReaders as ir

print("Day 4: Camp Cleanup");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#read file
areas = ir.read_oneline_records_as_list_entries(puzzle_file)

print (areas)

def is_overlap(area1,area2):
    overlap = False
    # area1 within area2
    if ((area1[0]>=area2[0])  and (area1[1]<=area2[1])) or\
    ( (area2[0]>=area1[0]) and (area2[1]<=area1[1])):

        print ("{} and {} overlap".format(area1,area2))
        overlap = True

    return overlap

def extract_areas (pair):
    areas=pair.replace("-",",").split(",")
    return [int(a) for a in areas]

num_overlaps = 0
for pair in areas:
    print (pair)
    area = extract_areas(pair)
    if is_overlap(area[0:2],area[2:4]):
        num_overlaps += 1


print ("Part 1: number of overlapping pairs is: {}".format(num_overlaps))

sys.exit(0)
priorities = 0

for team_num in range(0,len(backpacks),3):
    team_check = 0
    team_load = sorted(backpacks[team_num : team_num+3],key=len)
    for item in team_load [0] :
        if item in  team_load [1] and item in team_load [2]:
            priorities += get_priority (item)
            break

print ("Part 2: the total priority is: {}".format(priorities))
