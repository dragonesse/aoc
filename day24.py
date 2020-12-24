import sys
import utils.inputReaders as ir
import utils.locationHelpers as lh
print("Day 24: Lobby Layout");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

layout = ir.read_oneline_records_as_list_entries(puzzle_file)

tiles ={}

def pos2str (position):
    return str(position[0])+","+str(position[1])

def get_direction (pattern):
    if pattern[0:2] in ["se","ne","sw","nw"]:
        return pattern[0:2]
    else:
        return pattern[0]

for tile in layout:
    pat_ind = 0
    position = [0,0]
    while pat_ind < len(tile):
       direct = get_direction (tile[pat_ind:])
       position = lh.move_by_direction_on_hex_grid (position, direct)
       pat_ind += len(direct)
    str_pos = pos2str(position)
    if str_pos in tiles:
        tiles[str_pos] = "b" if tiles[str_pos] == "w" else "w"
    else:
        tiles[str_pos] = "b"


def get_number_adjacent_blacks (cur_pos, floor):
    directions = ["ne","se","sw","nw","e","w"]
    blk_cntr = 0
    for direct in directions:
        chk_pos = pos2str(lh.move_by_direction_on_hex_grid (cur_pos, direct))
        if chk_pos in floor:
            if floor[chk_pos] == "b":
                blk_cntr +=1
    return blk_cntr

def str2pos (str_pos):
    return [int(i) for i in str_pos.split(",")]

def get_v_max_pos (floor):
    max_v = [0,0]

    for p in list(floor.keys()):
        [x_cur,y_cur] = str2pos(p)
        if (x_cur > max_v[0]) or (x_cur==max_v[0] and y_cur>max_v[1]):
            max_v [0] = x_cur
            max_v [1] = y_cur
    return max_v

def get_v_min_pos (floor):
    min_v = [0,0]

    for p in list(floor.keys()):
        [x_cur,y_cur] = str2pos(p)
        if x_cur < min_v[0] or (x_cur==min_v[0] and y_cur<min_v[1]):
            min_v[0] = x_cur
            min_v[1] = y_cur
    return min_v

def get_h_max_pos (floor):
    max_h = [0,0]

    for p in list(floor.keys()):
        [x_cur,y_cur] = str2pos(p)

        if y_cur > max_h[1] or (y_cur==max_h[1] and x_cur>max_h[0]):
            max_h[0] = x_cur
            max_h[1] = y_cur
    return max_h

def get_h_min_pos(floor):
    min_h = [0,0]

    for p in list(floor.keys()):
        [x_cur,y_cur] = str2pos(p)
        if y_cur < min_h[1] or (y_cur==min_h[1] and x_cur<min_h[0]):
            min_h[0] = x_cur
            min_h[1] = y_cur
    return min_h

def get_tile_color(cur_pos,floor):
    return "w" if pos2str(cur_pos) not in floor else floor[pos2str(cur_pos)]

def get_num_blacks(floor):
    num_black = 0
    for tile in tiles.values():
        if tile == "b":
            num_black += 1
    return num_black

print ("part 1: number of black tiles: %d" %(get_num_blacks(tiles)))

days = 100

for day in range(1, days + 1):
    hmin = get_h_min_pos(tiles)
    hmax = get_h_max_pos(tiles)
    vmin = get_v_min_pos(tiles)
    vmax = get_v_max_pos(tiles)

    tiles2flip =[]

    for ty in range(hmin[1]-4,hmax[1]+4,2):
        #check range for x in given row
        xmx, xmn = 0,0
        if ty%4 == 0:
            # x should be even
            xmn = vmin[0] if vmin[0]%2 == 0 else vmin[0] -1
            xmx = vmax[0] if vmax[0]%2 == 0 else vmax[0] +1
        else:
            # for odd rows
            xmn = vmin[0] if vmin[0]%2 else vmin[0] -1
            xmx = vmax[0] if vmax[0]%2 else vmax[0] +1
        for tx in range (xmn-4,xmx+4,2):

            cur_col = get_tile_color([tx,ty],tiles)
            blck_cntr = get_number_adjacent_blacks([tx,ty],tiles)
            white_cntr = 6 - blck_cntr
            if cur_col == "w" and blck_cntr ==2:
                tiles2flip+=[pos2str([tx,ty])]
            if cur_col == "b" and (blck_cntr==0 or blck_cntr>2):
                tiles2flip+=[pos2str([tx,ty])]
    for t in tiles2flip:
        if t in tiles:
            tiles[t] = "b" if tiles[t] == "w" else "w"
        else:
            tiles[t] = "b"
print ("Part 2: Day %d number of black tiles: %d" %(day,get_num_blacks(tiles)))