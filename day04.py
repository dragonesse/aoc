import re;
import sys;

print("Day 1 puzzle: Inverse captcha");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

def index_to_compare (cur_index, offset):
    calc_index = 0;
    if (cur_index < offset):
        calc_index = int(cur_index + offset);
    else:
        calc_index = offset - (2 * offset - cur_index);
    return calc_index;

#open file
with open(puzzle_file, 'r') as puzzle_in:
    for cur_line in puzzle_in:
        digits = cur_line.strip("\n");
puzzle_in.close();

captcha_sum = 0;
# calculate the offset to digit taken for comparison
if (len(digits)%2 == 0):
    index_offset = int(len(digits)/2);
else:
    print ("The input has odd number of digits, exiting");
    sys.exit();

# process captcha calculation
digit_index = 0;
for digit_index in range (len(digits)):
    comp_index = index_to_compare (digit_index, index_offset);

    if (digits[digit_index] == digits[comp_index]):
        # incremetnt captcha sum
        captcha_sum += int(digits [digit_index]);

print ("The captcha sum is: %d" %(captcha_sum));