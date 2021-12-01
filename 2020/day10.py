import sys
import utils.inputReaders as ir

print("Day 10: Adapter Array");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

adapters = ir.read_int_records_as_list_entries(puzzle_file)

# this is charging socket
adapters += [0]
# this is the charged device
adapters += [max(adapters)+3]

adapters.sort()

one_jolt_cntr =0
three_jolts_cntr =0
for i in range (len(adapters)-1):
    jolt_diff = adapters[i+1] - adapters[i]
    if jolt_diff == 1:
        one_jolt_cntr +=1
    elif jolt_diff ==3:
        three_jolts_cntr += 1
    elif jolt_diff>3:
        print ("joltage difference in chain is too high")

print ("part 1: the joltage distribution is: %d" %(one_jolt_cntr*three_jolts_cntr))

# add meaningless stuff at the end to enable processing
# last elements in a wider context
adapters += [max(adapters)+3]
adapters += [max(adapters)+3]
adapters += [max(adapters)+3]
adapters += [max(adapters)+3]


i = 0
num_combinations = 1
while i < len(adapters) - 4:

    a0, a1 = adapters[i],adapters[i+1]
    a2, a3 = adapters[i+2], adapters[i+3]
    a4 = adapters[i+4]
    # can we remove a1 with keeping rules?
    if a2 - a0 <=3:
        #can we remove a2 adapter as well?
        if a3 - a1 <=3:
            # can third adapter an a row be removed?
            if a4-a2 <=3:
                # removing three elems gives 7 possibilities
                i+=4
                num_combinations *=7
            else:
                # removal of exactly two elements
                i+=3
                num_combinations *=4
        else:
        #removal of one element multiplies possibilities by 2
            i+=1
            num_combinations *= 2
    # a1 stays
    else:
        i+=1

print ("part 2: num_combinations %d" %(num_combinations))
