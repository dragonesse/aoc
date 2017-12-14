import sys;
import itertools;
import functools;

print("Day 14 puzzle: Disk Defragmentation");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

def update_iterator (offset, len_list, iterator):
    if offset%len_list > 0:
        iterator= itertools.islice(iterator, offset%len_list , None);
    return iterator;

def make_iterator (list_len, offset = 0):
    it = itertools.cycle([x for x in range(list_len)]);
    if offset > 0:
        it = update_iterator(offset, list_len, it);
    return it;

def get_substr (start,num_elems,src_list):
    substr = [];
    it = make_iterator(len(src_list),start);

    for i in range(num_elems):
        substr = substr + [ src_list[next(it)] ];

    return substr;

def put_substr (start,list2put,targ_list):

    it = make_iterator(len(targ_list),start);
    for char in list2put:
        targ_list[next(it)] = char;

    return targ_list;

def calc_start (old_start, len2move, skip_s, len_list):
    it = make_iterator(len_list,old_start + (len2move + skip_s)%len_list);

    return next(it);

#open file
lengths = [];
suffix = [17, 31, 73, 47, 23];
with open(puzzle_file, 'r') as puzzle_in:

    for cur_line in puzzle_in:
        lengths = [ord(x) for x in cur_line.strip("\n")];

puzzle_in.close();

list_len = 256;
binstr = [];
allocated = 0;
allocations = [];

for row in range (128):
    list_to_hash = [x for x in range(list_len)];
    start_pos  = 0;
    skip_size  = 0;

    hash_seed = lengths + [ord("-")] + [ord(x) for x in str(row)] + suffix;

    for rnd_id in range (64):
        for single_len in hash_seed:
            # get substring

            if single_len > 0:
                substr = get_substr (start_pos,single_len,list_to_hash);
                # reverse it
                substr = substr[::-1];
                list_to_hash = put_substr(start_pos,substr,list_to_hash);
            else:
                print ("zero length substr, calculating next move")

            # recalculate positions to next iteration
            start_pos = calc_start(start_pos,single_len,skip_size,len(list_to_hash));
            skip_size += 1;

    # calculate dense hash - xor groups of 16 bytes
    dense_hash = [];

    for k in range(16):
        dense_hash += [functools.reduce(lambda i, j: i^j, list_to_hash[k*16:16 + k*16])];

    hexstr = ''.join([format(x, '#04x') for x in dense_hash]).replace("0x","");
    binstr = ''.join(format (int(x,16), '#06b')for x in hexstr).replace("0b","");
    allocated += binstr.count("1");
    allocations.append([int(x) for x in list(binstr)]);

print ("disc usage is %d blocks: " %(allocated));

def is_region (position,allocations):
    answer = False
    x = position[0];
    y = position [1];

    # we assume square shaped disc
    size_x = len(allocations[0]);
    size_y = size_x;

    # we need to filter out of range inputs
    if (x >= 0) and (x < size_x) and (y >= 0) and (y < size_y) :
        # check for currently stored value
        if allocations[x][y] == 1:
            answer = True;

    return answer;

def block_update (position, allocations):
    x = position[0];
    y = position[1];
    if allocations[x][y] == 1:
        allocations[x][y] = 9;
    return;

def regionalize (position, allocations):
    neighbours = [];
    x = position[0];
    y = position[1];
    blocks_in_reg = 0;
    if is_region (position,allocations):
        blocks_in_reg += 1;
        block_update (position, allocations);
        # search for neighbours
        for neigb_cand in [[x, y+1],[x, y -1],[x + 1, y],[x-1, y]]:
            blocks_in_reg += regionalize (neigb_cand, allocations);

    return blocks_in_reg;

num_blocks = 128;
p = [0,0];

regions = 0;

for i in range(num_blocks*num_blocks):

    if regionalize(p, allocations) > 0:
        regions += 1;

    if p[1] < num_blocks - 1:
        p[1] += 1;
    elif p[0] < num_blocks - 1:
        p[1] = 0;
        p[0] += 1;

print ("number of regions: %d" %(regions));
