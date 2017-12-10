import re;
import sys;

print("Day 10 puzzle: Knot Hash");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

def get_substr (start,num_elems,src_list):
    substr = "";

    if start + num_elems > len(src_list):
        substr = src_list[start:] + src_list [:num_elems - (len(src_list) - start)];
    else:
        substr = src_list[start:start+num_elems];

    return substr;

def put_substr (start,list2put,targ_list):

    if len(list2put) < len(targ_list) - start:
        targ_list[start:start + len(list2put)] = list2put;
    else:
        targ_list[start:] = list2put[:len(targ_list)-start];
        targ_list[:len(list2put) - (len(targ_list)-start)] = list2put[len(targ_list)-start:];

    return targ_list;

def calc_start (old_start, len2move, skip_s, len_list = 256):
    new_start = 0;
    if old_start + len2move + skip_s < len_list:
        new_start = old_start + len2move + skip_s;
    else:
        new_start = (len2move + skip_s ) - (len_list - old_start);

    return new_start;

#open file
lengths = [];
with open(puzzle_file, 'r') as puzzle_in:

    for cur_line in puzzle_in:
        lengths = [int(x) for x in cur_line.split(r",")];

puzzle_in.close();


list_to_hash = [x for x in range(256)];
start_pos  = 0;
skip_size  = 0;

for single_len in lengths:
    # get substring
    print ("\nhashed list before: %s" %(list_to_hash));
    print ("slice length %d, skip size %d, start %d" %(single_len,skip_size,start_pos));

    substr = get_substr (start_pos,single_len,list_to_hash);
    # reverse it
    substr = substr[::-1];
    print ("substring ", substr);

    list_to_hash = put_substr(start_pos,substr,list_to_hash);
    start_pos = calc_start(start_pos,single_len,skip_size,len(list_to_hash));
    skip_size += 1;

    print ("hashed list after: %s" %(list_to_hash));
    print ("multiplication of first two items: %d" %(list_to_hash[0] * list_to_hash [1]));