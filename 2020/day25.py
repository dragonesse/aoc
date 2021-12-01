import sys
import utils.inputReaders as ir
print("Day 25: Combo Breaker");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

pub_keys = ir.read_int_records_as_list_entries(puzzle_file)

door_loop_cntr = 0
card_loop_cntr = 0

def transform_sn (num_loops, sn,start_loop=1,start_val=1):
    val = start_val
    magic_num = 20201227
    for lp in range(start_loop,num_loops+1):
        val = (val*sn)%magic_num
    return val

def find_loop_val (expected_pub_key):
    calc_pub_key = 1
    loop_cntr = 0
    subj_num = 7
    while (calc_pub_key != expected_pub_key) :
        loop_cntr += 1
        calc_pub_key = transform_sn(loop_cntr,subj_num,loop_cntr,calc_pub_key)

    print ("Loop val %d keys are equal: " %loop_cntr, calc_pub_key == expected_pub_key)
    return loop_cntr

card_loop_cntr = find_loop_val(pub_keys[0])
door_loop_cntr = find_loop_val(pub_keys[1])

encr_key_by_card = transform_sn(card_loop_cntr,pub_keys[1])
encr_key_by_door = transform_sn(door_loop_cntr,pub_keys[0])

print ("Encryption key: %d keys match: " %encr_key_by_card, encr_key_by_card==encr_key_by_door)