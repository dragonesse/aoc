import sys
import utils.inputReaders as ir
import utils.locationHelpers as lh
print("Day 12: Rain Risk");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

directions = ir.read_oneline_records_as_list_entries(puzzle_file)


def move_north (amount, cur_pos):
    return  [cur_pos[0], cur_pos [1] + amount]

def move_south (amount, cur_pos):
    return  [cur_pos[0], cur_pos [1] - amount]

def move_east (amount, cur_pos):
    return  [cur_pos[0] + amount, cur_pos [1]]

def move_west (amount, cur_pos):
    return  [cur_pos[0] - amount, cur_pos [1]]

def move_forward (amount, cur_pos,cur_dir):
    return movements[cur_dir](amount,cur_pos)

def turn_right (amount, cur_dir):
    next_right=["S","W","N","E"]
    index_now = next_right.index(cur_dir)
    index_next = lh.move_one_dimension_wrapped(index_now,int(amount/90),4)
    return next_right[index_next]

def turn_left (amount, cur_dir):
    next_left = ["N","W","S","E"]
    index_now = next_left.index(cur_dir)
    index_next = lh.move_one_dimension_wrapped(index_now,int(amount/90),4)
    return next_left[index_next]

movements ={
    "N": move_north,
    "S": move_south,
    "E": move_east,
    "W": move_west
}
def move(direction, amount, cur_pos, cur_dir):
    if direction == "N":
        cur_pos = move_north (amount,cur_pos)
    if direction == "S":
        cur_pos = move_south (amount,cur_pos)
    if direction == "E":
        cur_pos = move_east (amount,cur_pos)
    if direction == "W":
        cur_pos = move_west (amount,cur_pos)
    if direction == "F":
        cur_pos = move_forward(amount,cur_pos,cur_dir)
    if direction == "R":
        cur_dir = turn_right (amount, cur_dir)
    if direction == "L":
        cur_dir = turn_left (amount, cur_dir)

    return [cur_pos,cur_dir]

cur_pos = [0,0]
cur_dir = "E"

for mv in directions:
    move_type = mv[0]
    move_dist = int(mv[1:])
    [cur_pos,cur_dir] = move(move_type,move_dist,cur_pos,cur_dir)

print ("The final position is: ", cur_pos)
print ("part 1: The distance is: %d" %(lh.get_manhattan_dist([0,0],cur_pos)))

def get_waypoint_ship_relation (pos_waypoint,pos_ship):
    horiz_relation = ""
    vert_relation = ""
    if pos_waypoint[0] - pos_ship[0]>0:
        horiz_relation = "E"
    else:
        horiz_relation = "W"
    if pos_waypoint[1] - pos_ship[1]>0:
        vert_relation = "N"
    else:
        vert_relation = "S"
    return [horiz_relation,vert_relation]

def get_relative_pos (pos_ship,pos_waypoint):
    [rh,rv] = get_waypoint_ship_relation(pos_waypoint,pos_ship)
    return str(abs(pos_ship[0]-pos_waypoint[0]))+rh+str(abs(pos_ship[1]-pos_waypoint[1]))+rv

def rotate_1step(new_qarter, pos_ship,pos_waypoint):
    dist_x = abs(pos_ship[0] -pos_waypoint[0])
    dist_y = abs(pos_ship[1] -pos_waypoint[1])
    nz_dist = dist_x if dist_x > 0 else dist_y
    rotation_val = {
        "E"  : [pos_ship[0] + nz_dist, pos_ship[1]],
        "ES" : [pos_ship[0] + dist_y, pos_ship[1] - dist_x],
        "S"  : [pos_ship[0], pos_ship[1] - nz_dist],
        "WS" : [pos_ship[0] - dist_y, pos_ship[1] - dist_x],
        "W"  : [pos_ship[0]- nz_dist, pos_ship[1]],
        "WN" : [pos_ship[0] - dist_y, pos_ship[1] + dist_x],
        "N"  : [pos_ship[0], pos_ship[1] + nz_dist],
        "EN" : [pos_ship[0] + dist_y, pos_ship[1] + dist_x]
    }

    return rotation_val[new_qarter]

def rotate_waypoint(rot_dir,amount, pos_waypoint,pos_ship):
    [rh,rv] = get_waypoint_ship_relation(pos_waypoint,pos_ship)
    dist_x = abs(pos_ship[0] -pos_waypoint[0])
    dist_y = abs(pos_ship[1] -pos_waypoint[1])

    cur_rel = ""
    rotations_order = []
    if dist_y>0 and dist_y >0 :
        cur_rel = rh+rv
        if rot_dir == "R":
            rotations_order = ["EN","ES","WS","WN"]
        else:
            rotations_order = ["EN","WN","WS","ES"]
    elif dist_y == 0 or dist_x ==0:
        cur_rel = rh if dist_x > 0 else rv
        if rot_dir == "R":
            rotations_order = ["E","S","W","N"]
        else:
            rotations_order = ["E","N","W","S"]
    elif dist_x==0 and dist_y == 0:
        return pos_waypoint

    rot_cntr = int(amount/90)
    tmp_pos = [pos_waypoint[0],pos_waypoint[1]]
    while rot_cntr > 0:
        cur_rot_ind = rotations_order.index(cur_rel)
        next_rot_ind = lh.move_one_dimension_wrapped(cur_rot_ind,1,4)

        tmp_pos = rotate_1step(rotations_order[next_rot_ind],pos_ship,tmp_pos)
        rot_cntr -=1
        cur_rel = rotations_order[next_rot_ind]

    return tmp_pos

ship_pos = [0,0]
waypoint_pos = [10,1]
for mv in directions:
    move_type = mv[0]
    move_dist = int(mv[1:])
    [rh,rv] = get_waypoint_ship_relation(waypoint_pos,ship_pos)
    if move_type == "F":
        [mht,mvt] =get_waypoint_ship_relation(waypoint_pos,ship_pos)
        mhd = move_dist*abs(waypoint_pos[0]-ship_pos[0])
        mvd = move_dist*abs(waypoint_pos[1]-ship_pos[1])
        ship_pos = move_forward(mhd,ship_pos,mht)
        ship_pos = move_forward(mvd,ship_pos,mvt)
        waypoint_pos = move_forward(mhd,waypoint_pos,mht)
        waypoint_pos = move_forward(mvd,waypoint_pos,mvt)
    if move_type in ["N","S","E","W"]:
        waypoint_pos = movements[move_type](move_dist,waypoint_pos)
    if move_type in ["L", "R"]:
        waypoint_pos = rotate_waypoint(move_type,move_dist, waypoint_pos,ship_pos)

print ("The final position is: ", ship_pos)
md = lh.get_manhattan_dist([0,0],ship_pos)
print ("part 2: The distance is: %d" %(md))

if False:
    print ("----test R1")
    assert rotate_waypoint ("R", 90, [10,1], [0,0]) == [1, -10]
    assert rotate_waypoint ("R", 180, [10,1], [0,0]) == [-10,-1]
    assert rotate_waypoint ("R", 270, [10,1], [0,0]) == [-1, 10]
    print ("----test R2")
    assert rotate_waypoint ("R", 90, [1,-10], [0,0]) == [-10,-1]
    assert rotate_waypoint ("R", 180, [1,-10], [0,0]) == [-1, 10]
    assert rotate_waypoint ("R", 270, [1,-10], [0,0]) == [10,1]
    print ("----test R3")
    assert rotate_waypoint ("R", 90, [-10,-1], [0,0]) == [-1,10]
    assert rotate_waypoint ("R", 180, [-10,-1],[0,0]) == [10,1]
    assert rotate_waypoint ("R", 270, [-10,-1], [0,0]) == [1,-10]
    print ("----test R4")
    assert rotate_waypoint ("R", 90, [-1,10],[0,0]) == [10,1]
    assert rotate_waypoint ("R", 180, [-1,10],[0,0]) ==[1,-10]
    assert rotate_waypoint ("R", 270, [-1,10], [0,0]) == [-10,-1]

    print ("----test L1")
    assert rotate_waypoint ("L", 90, [10,1], [0,0]) == [-1, 10]
    assert rotate_waypoint ("L", 180, [10,1], [0,0]) == [-10,-1]
    assert rotate_waypoint ("L", 270, [10,1], [0,0]) == [1, -10]
    print ("----test L2")
    assert rotate_waypoint ("L", 90, [1,-10], [0,0]) == [10,1]
    assert rotate_waypoint ("L", 180, [1,-10], [0,0]) == [-1, 10]
    assert rotate_waypoint ("L", 270, [1,-10], [0,0]) == [-10,-1]
    print ("----test L3")
    assert rotate_waypoint ("L", 90, [-10,-1], [0,0]) == [1,-10]
    assert rotate_waypoint ("L", 180, [-10,-1],[0,0]) == [10,1]
    assert rotate_waypoint ("L", 270, [-10,-1], [0,0]) == [-1,10]
    print ("----test L4")
    assert rotate_waypoint ("L", 90, [-1,10],[0,0]) == [-10,-1]
    assert rotate_waypoint ("L", 180, [-1,10],[0,0]) ==[1,-10]
    assert rotate_waypoint ("L", 270, [-1,10], [0,0]) == [10,1]
