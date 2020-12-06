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