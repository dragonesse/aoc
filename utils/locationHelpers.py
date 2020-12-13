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