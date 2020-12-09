import sys
import utils.inputReaders as ir

print("Day 7 puzzle: Encoding Error");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

enc_stream = ir.read_int_records_as_list_entries(puzzle_file)

# print(enc_stream)

# for test data
preamble_len = 25
stream_index = preamble_len-1

def validate_preamble_sum(pr_len,start_ind, exp_res):
    # print ("indexes to scrutiny: ", list(range(start_ind - (pr_len-1),start_ind)))
    for i in range(start_ind - (pr_len-1),start_ind): #last is 24
        # print ("processing %d" %enc_stream[i])
        for k in range (1,start_ind-i+1):
            # print ("compare with %d" %enc_stream[i+k])
            if enc_stream[i]+enc_stream[i+k]==exp_res:
                # print("the sum matches")
                return True
            # else:
            #     print("+++the sum is: %d" %(enc_stream[i]+enc_stream[i+1+k]))
    print ("No matching combination of preamble gives %d" %exp_res)
    return False


for i in enc_stream[preamble_len:]:
    print ("====== checking item %d" %i)
    if not validate_preamble_sum(preamble_len,stream_index,i):
        print ("found first item that does not comply XMAS rule %d" %i)
        break

    stream_index +=1
