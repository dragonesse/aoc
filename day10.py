import re;
import sys;
import itertools;

print("Day 10 puzzle: Knot Hash");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

def update_iterator (offset, len_list, iterator):
    if offset%len_list > 0:
        print ("update_iterator: offset", offset);
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

    # if start + num_elems > len(src_list):
    #     substr = src_list[start:] + src_list [:num_elems - (len(src_list) - start)];
    # else:
    #     substr = src_list[start:start+num_elems];

    pr = 1;
    for i in range(num_elems):
        n = next (it);
        if pr:
            print ("get_substr: first index in src_list", n);
            pr = 0;
        substr = substr + [src_list[n ]];

    return substr;

def put_substr (start,list2put,targ_list):

    # if len(list2put) < len(targ_list) - start:
    #     targ_list[start:start + len(list2put)] = list2put;
    # else:
    #     targ_list[start:] = list2put[:len(targ_list)-start];
    #     targ_list[:len(list2put) - (len(targ_list)-start)] = list2put[len(targ_list)-start:];

    it = make_iterator(len(targ_list),start);
    pr = 1;
    for char in list2put:
        n = next(it);
        if pr:
            print ("put_substr: first index in targ_list", n);
            pr = 0;
        targ_list[n] = char;

    return targ_list;

def calc_start (old_start, len2move, skip_s, len_list):
    new_start = 0;
    # if old_start + ((len2move + skip_s)%len_list) < len_list:
    #     new_start = old_start + ((len2move + skip_s)%len_list);
    # else:
    #     new_start = ((len2move + skip_s )%len_list) - (len_list - old_start);
    it = make_iterator(len_list,old_start + (len2move + skip_s)%len_list);
    new_start = next(it);

    print ("calc_start: new start point is: ", new_start);
    return new_start;

#open file
lengths = [];
with open(puzzle_file, 'r') as puzzle_in:

    for cur_line in puzzle_in:
        lengths = [int(x) for x in cur_line.split(r",")];

puzzle_in.close();

list_len = 256;
list_to_hash = [x for x in range(list_len)];
start_pos  = 0;
skip_size  = 0;

cyclic_iterator = make_iterator(list_len);

for single_len in lengths:
    # get substring
    print ("\nhashed list before: %s" %(list_to_hash));
    print ("slice length %d, skip size %d, start %d" %(single_len,skip_size,start_pos));

    if single_len > 0:
        substr = get_substr (start_pos,single_len,list_to_hash);
        # reverse it
        substr = substr[::-1];
        print ("substring ", substr);
        list_to_hash = put_substr(start_pos,substr,list_to_hash);
    else:
        print ("zero length substr, calculating next move")

    print ("\nhashed list after: %s" %(list_to_hash));
    # input ("press the enter");

    # this update iterator
    # update_iterator(start_pos + single_len + skip_size - 1,len(list_to_hash),cyclic_iterator);
    start_pos = calc_start(start_pos,single_len,skip_size,len(list_to_hash));

    skip_size += 1;

print ("multiplication of first two items: %d" %(list_to_hash[0] * list_to_hash [1]));