def has_reach_bound (pos,size):
    return pos>=size

def move_one_dimension (init_pos, dist):
    return init_pos + dist

def move_one_dimension_wrapped (init_pos, dist, size):
    pos = None
    if has_reach_bound(init_pos + dist, size):
        pos =  (init_pos + dist) -(size)
    else:
        pos = init_pos + dist
    return pos

def move_two_dimensions (init_pos,dist):
    return [init_pos[0]+dist[0],init_pos[1]+dist[1]]

def get_manhattan_dist(start_pos,end_pos):
    return abs(end_pos[0]-start_pos[0])+abs(end_pos[1]-start_pos[1])

def move_by_direction_on_hex_grid (init_pos, direction):
    # the tile is a hexagon, placed in 3x2 grid
    # the starting point indicates left-upper corner
    # the possible directions are:
    # e, w, ne, nw, se, sw
    end_pos = []
    print ("starting from: ", init_pos, "moving %s" %(direction))
    if direction == "e":
        end_pos = [init_pos[0]+2,init_pos[1]]
    elif direction == "w":
        end_pos = [init_pos[0]-2,init_pos[1]]
    elif direction == "ne":
        end_pos = [init_pos[0]+1,init_pos[1]+2]
    elif direction == "nw":
        end_pos = [init_pos[0]-1,init_pos[1]+2]
    elif direction == "se":
        end_pos = [init_pos[0]+1,init_pos[1]-2]
    elif direction == "sw":
        end_pos = [init_pos[0]-1,init_pos[1]-2]
    print ("ending at: ", end_pos)
    return end_pos