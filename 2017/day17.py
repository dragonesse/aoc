import sys;

print("Day 17 puzzle: Spinlock ");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

offset = 0;

#open file
with open(puzzle_file, 'r') as puzzle_in:
    offset = int(puzzle_in.read().strip("\n"));

puzzle_in.close();

def calc_new_pos (index, cb_len, offset):
    np = index
    # from cur pos, move by offset
    # if the offsset is bigger than remaining part of buffer
    # wrap around

    if offset % cb_len <= cb_len -(index + 1):
        np = index + (offset % cb_len) + 1
    else:
        # calculate, num of tile to wrap
        np = (offset % cb_len ) - (cb_len - (index + 1))

    return np

max_num = int(50E6);
circ_buf_len = 1;
cur_index = 0;
num_to_store = 1;
val_at_p1   = None;

print ("spinlock starts....")
# we need to stop at 50th million operation and get the status before insert happens
while num_to_store < max_num :
    # spinlock moves forward

    cur_index = calc_new_pos (cur_index,circ_buf_len, offset);
    if cur_index == 1:
        val_at_p1 = num_to_store;

    num_to_store += 1
    circ_buf_len += 1

print ("the tile next to 0 is: ", val_at_p1 );