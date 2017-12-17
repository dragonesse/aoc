import sys;
import itertools;

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

def update_iterator (offset, len_list, iterator):
    if offset%len_list > 0:
        iterator= itertools.islice(iterator, offset%len_list , None);
    return iterator;

def make_iterator ( list_len, offset = 0):
    it = itertools.cycle([x for x in range(list_len)]);
    if offset > 0:
        it = update_iterator(offset, list_len, it);
    return it;

def calc_new_pos (index, cb_len, offset):
    it = make_iterator ( cb_len, (index + offset));

    return next(it) + 1;


max_num = 2017;
# max_num = int(50E6);
circ_buff = [0];

cur_index = 0;
num_to_store = 1;

print ("spinlock starts....")
while num_to_store < max_num + 1:
    if not num_to_store%10000:
        print ("iteration %d, still %d left" %(num_to_store, (max_num - num_to_store)))
    # spinlock moves forward

    cur_index = calc_new_pos (cur_index,len(circ_buff), offset);
    # print ("number %d to be stored at index %d" %(num_to_store,cur_index));
    circ_buff.insert( cur_index, num_to_store);

    # print (num_to_store, len(circ_buff), circ_buff[:10]);
    # input ("press enter");
    # cur_index = num_to_store;
    num_to_store += 1

print ("the tile next to 0 is: ", circ_buff[circ_buff.index(2017) + 1 ]);



