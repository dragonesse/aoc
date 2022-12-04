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

def is_included(area1,area2):
    include = False
    if ((area1[0]>=area2[0])  and (area1[1]<=area2[1])) or\
    ( (area2[0]>=area1[0]) and (area2[1]<=area1[1])):
        include = True

    return include

def is_overlap(area1,area2):
    overlap = False
    if ((area1[1]<=area2[1]) and (area1[1]>=area2[0])) or\
        ((area2[1]<=area1[1]) and (area2[1]>=area[0])):
        overlap = True

    return overlap


def extract_areas (pair):
    areas=pair.replace("-",",").split(",")
    return [int(a) for a in areas]

num_includes = 0
num_overlaps = 0
for pair in areas:
    area = extract_areas(pair)
    if is_included(area[0:2],area[2:4]):
        num_includes += 1
    if is_overlap(area[0:2],area[2:4]):
        num_overlaps += 1


print ("Part 1: number of pairs that mutually include: {}".format(num_includes))
print ("Part 2: the number of overlaps is: {}".format(num_overlaps))


