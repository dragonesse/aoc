import sys
import string

print("Day 6 puzzle: Chronal Coordinates");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#open file
coordinates = []

with open(puzzle_file, 'r') as puzzle_in:

    for cur_line in puzzle_in:
        x = int(cur_line.split(",")[0].strip())
        y = int(cur_line.split(",")[1].strip())
        coordinates.append([x,y])
puzzle_in.close()

print (coordinates)

sorted_by_y = sorted(coordinates, key=lambda x:x[1])
sorted_by_x = sorted(coordinates, key=lambda x:x[0])
[min_y, max_y] = [sorted_by_y[0][1],sorted_by_y[-1][1]]
[min_x, max_x] = [sorted_by_x[0][0],sorted_by_x[-1][0]]

[top_c,left_c,right_c,down_c] = [sorted_by_y[0],sorted_by_x[0],sorted_by_x[-1],sorted_by_y[-1]]

print ("top left right down", top_c,left_c,right_c,down_c)
print ("will process from: ", [min_x, min_y], "to ", [max_x, max_y])

def get_cab_distance (start_x,start_y,end_x,end_y):
    return abs(end_x - start_x) + abs(end_y - start_y)

def convert_coord_to_string (x,y):
    return str(x)+"-"+str(y)

def get_x_from_key (key):
    return int(key[0])

def get_y_from_key (key):
    return int(key[-1])

# from minx,miny to maxx,maxy
# get all the points and try to calculate distance to
# any of given coordinates
max_dist = get_cab_distance(min_x,min_y,max_x,max_y)
areas = {}
for y in range(min_y,max_y + 1):
    for x in range (min_x,max_x + 1):
        dist_to_comp = max_dist
        winning_loc = []
        for target_loc in coordinates:
            cur_dist = get_cab_distance(x,y,target_loc[0],target_loc[1])
            # we hit the coordinate, no point to process
            if cur_dist == 0:
                print ([x,y], " hit the exact coordinate", target_loc)
                winning_loc = target_loc
                dist_to_comp = 0
                break
            elif cur_dist < dist_to_comp:
                dist_to_comp = cur_dist
                winning_loc = target_loc.copy()
            elif cur_dist == dist_to_comp:
                print ([x,y], " has a tie, reset winner")
                winning_loc = []
                # break
        if len(winning_loc):
            print ([x,y], " is closest to ", winning_loc, " the distance is ", dist_to_comp )
            coord_key = convert_coord_to_string(winning_loc[0],winning_loc[1])
            if coord_key not in areas:
                areas[coord_key] = 1
            else:
                areas[coord_key] = areas[coord_key] + 1

# border areas are always infinite, remove them from list of entries
print (areas)

for c in areas.keys():
    if get_x_from_key(c) == min_x or get_x_from_key(c) == max_x:
        areas[c] = -1
    elif get_y_from_key(c) ==min_y or get_y_from_key(c) == max_y:
        areas[c] = -1

print ("The biggest area is ", max(areas.values()))








