import sys

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

def get_cab_distance (start_x,start_y,end_x,end_y):
    return abs(end_x - start_x) + abs(end_y - start_y)

def convert_coord_to_string (x,y):
    return str(x)+"-"+str(y)

def get_x_from_key (key):
    return int(key[0])

def get_y_from_key (key):
    return int(key[-1])

# part 1
sorted_by_y = sorted(coordinates, key=lambda x:x[1])
sorted_by_x = sorted(coordinates, key=lambda x:x[0])
[min_y, max_y] = [sorted_by_y[0][1],sorted_by_y[-1][1]]
[min_x, max_x] = [sorted_by_x[0][0],sorted_by_x[-1][0]]

[top_c,left_c,right_c,down_c] = [sorted_by_y[0],sorted_by_x[0],sorted_by_x[-1],sorted_by_y[-1]]

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
                winning_loc = target_loc
                dist_to_comp = 0
                break
            # new closest
            elif cur_dist < dist_to_comp:
                dist_to_comp = cur_dist
                winning_loc = target_loc.copy()
            # a tie, reset the winner
            elif cur_dist == dist_to_comp:
                winning_loc = []
        if len(winning_loc):
            coord_key = convert_coord_to_string(winning_loc[0],winning_loc[1])
            if coord_key not in areas:
                areas[coord_key] = 1
            else:
                areas[coord_key] = areas[coord_key] + 1

# border areas are always infinite, remove them from list of entries
for c in areas.keys():
    if get_x_from_key(c) == min_x or get_x_from_key(c) == max_x:
        areas[c] = -1
    elif get_y_from_key(c) ==min_y or get_y_from_key(c) == max_y:
        areas[c] = -1
print (areas)

print ("The biggest area is ", max(areas.values()))

# part two
def is_safe (x, y, safe_dist, coordinates):
    dist_to_comp = 0
    for target_loc in coordinates:
        dist_to_comp += get_cab_distance(x,y,target_loc[0],target_loc[1])

    return dist_to_comp < safe_dist

# calculate safe region
regions = []
# safe_distance = 32
safe_distance = 10000

for [cx,cy] in coordinates:
    # build safe areas around coordinates
    print ("\nchecking around coordinate ", [cx,cy])
    safe_flag = True
    side_len = 1
    region_size = 0

    while safe_flag:
        safe_flag = False
        if side_len == 1:
            if not is_safe(cx,cy,safe_distance,coordinates):
                print ("can't build around coordinates, if they are unsafe")
                break
            else:
                region_size += 1

        for y in range(cy-side_len, cy+side_len+1):
            if y == cy-side_len or y == cy+side_len:
                for x in range(cx-side_len, cx+side_len+1):
                    if is_safe(x, y, safe_distance, coordinates):
                        safe_flag = True
                        region_size += 1
            else:
                for x in [cx-side_len, cx+side_len]:
                    if is_safe(x, y, safe_distance, coordinates):
                        safe_flag = True
                        region_size += 1
        side_len += 1
    print ("overall region size is: ", region_size)
    regions.append(region_size)

print ("The biggest safe region is: ", max(regions))