import sys
import math
print("Day 3 puzzle: Crossed Wires");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#open file
wire1 = []
wire2 = []

with open(puzzle_file, 'r') as puzzle_in:
    wire1 = puzzle_in.readline().strip("\n").split(",")
    wire2 = puzzle_in.readline().strip("\n").split(",")
puzzle_in.close()

cordinates_w1 = []
cordinates_w2 = []
def calc_manhattan_dist (x1, y1, x2, y2):
    return abs (x2-x1) + abs (y2-y1)

def transpond (guideline,location_arry):
    direction = guideline[0]
    length = int(guideline[1:])
    start_coordinate = get_last_pos(location_arry)
    if direction == "U":
        end_coordinate = (start_coordinate[0],start_coordinate[1] + length )
    elif direction == "D":
        end_coordinate = (start_coordinate[0],start_coordinate[1] - length )
    elif direction =="R":
        end_coordinate = (start_coordinate[0] + length,start_coordinate[1])
    else:
        end_coordinate = (start_coordinate[0] - length,start_coordinate[1])
    return [start_coordinate,end_coordinate]

def get_last_pos (location_arry):
    return location_arry[-1][1] if len(location_arry)>0 else (0,0)

def is_vertical(section):
    return section[0][0] == section[1][0]
def is_horizontal(section):
    return section[0][1] == section[1][1]
def is_inside(p1, ps, pe):
    return ((p1 >= ps) and (p1 <= pe)) or ((p1 <= ps) and (p1 >= pe))

def calc_cross_point (section1,section2):
    # section 1 x is between section 2 x1 and x2 AND
    # section 2 y is between section 1 y1 and y2
    if is_vertical(section1) and \
        is_horizontal(section2) and \
        is_inside (section2[0][1], section1[0][1], section1[1][1]) and \
        is_inside (section1[0][0], section2[0][0], section2[1][0]):
        return (section1[0][0],section2[0][1])
    if is_vertical(section2) and \
        is_horizontal(section1) and \
        is_inside (section1[0][1], section2[0][1], section2[1][1]) and \
        is_inside (section2[0][0], section1[0][0], section1[1][0]):
        return (section2[0][0],section1[0][1])

    return None

for guideline in wire1:
    cordinates_w1.append(transpond(guideline,cordinates_w1))

for guideline in wire2:
    cordinates_w2.append(transpond(guideline,cordinates_w2))

min_dist_by_len = []
min_dist_by_time = []
start_point = (0,0)
dist_w1 = 0
dist_w2 = 0
for i in range(len(cordinates_w2)):
    section2 = cordinates_w2[i]
    dist_w2 += int(wire2[i][1:])
    dist_w1 = 0
    for k in range(len(cordinates_w1)):
        section1 = cordinates_w1[k]
        dist_w1 += int(wire1[k][1:])
        intersection = calc_cross_point(section2,section1)
        if intersection is not None:

            dist = calc_manhattan_dist(intersection[0],intersection[1], start_point[0],start_point[1])
            if dist>0:
                min_dist_by_len.append(dist)
                # decrement distance
                if is_horizontal (section1):
                    dist_w1_tmp = dist_w1 - abs(section1[1][0] - intersection[0])
                    dist_w2_tmp = dist_w2 - abs(section2[1][1] - intersection[1])
                else:
                    dist_w1_tmp = dist_w1 - abs(section1[1][1] - intersection[1])
                    dist_w2_tmp = dist_w2 - abs(section2[1][0] - intersection[0])
                min_dist_by_time.append(dist_w2_tmp + dist_w1_tmp)

print("the min distance by length is", min(min_dist_by_len))
print ("the min distance by time is", min(min_dist_by_time))