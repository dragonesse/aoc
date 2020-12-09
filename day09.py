import sys
import utils.inputReaders as ir

print("Day 9 puzzle: Encoding Error");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

enc_stream = ir.read_int_records_as_list_entries(puzzle_file)

# for test data change this value to 5
preamble_len = 25
stream_index = preamble_len-1

def validate_preamble_sum(pr_len,start_ind, exp_res):
    for i in range(start_ind - (pr_len-1),start_ind):
        for k in range (1,start_ind-i+1):
            if enc_stream[i]+enc_stream[i+k]==exp_res:
                return True
    print ("No matching combination of preamble gives %d" %exp_res)
    return False

invalid_num = 0
for i in enc_stream[preamble_len:]:
    if not validate_preamble_sum(preamble_len,stream_index,i):
        print ("found first item that does not comply XMAS rule %d" %i)
        #needed for part 2
        invalid_num = i
        break
    stream_index +=1

found_sum = False
for i in range(stream_index-1):
    grand_total = enc_stream[i]
    sum_list = [enc_stream[i]]

    if found_sum:
        # there could be much more items, but no need to continue
        print("bye, bye, nothing else to do")
        break
    if enc_stream[i] > invalid_num:
        print ("greater item cannot sum up to smaller, resetting results")
        grand_total = 0
        sum_list = []
        continue
    else:
        for k in range (i+1,stream_index):
            grand_total += enc_stream[k]
            sum_list += [enc_stream[k]]
            if grand_total == invalid_num:
                print ("found sequence that adds up to %d " %invalid_num, sum_list)
                print ("the min-max sum is %d" %(min(sum_list)+max(sum_list)))
                found_sum = True
                break

