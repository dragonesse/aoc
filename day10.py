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

print ("1-joltage frequency %d, 3-joltage frequency %d" %(one_jolt_cntr,three_jolts_cntr))
print ("the joltage distribution is: %d" %(one_jolt_cntr*three_jolts_cntr))
