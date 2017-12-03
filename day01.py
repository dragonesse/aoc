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

captcha_sum = 0;

#open file
with open(puzzle_file, 'r') as puzzle_in:
    for cur_line in puzzle_in:
        digits = cur_line.strip("\n");
puzzle_in.close();

# process commands
digit_index = 0;
for digit_index in range (len(digits) - 1):
    print ("processing index %d, digit %s" %(digit_index, digits[digit_index]));
    if (digits[digit_index] == digits[digit_index + 1]):
        # incremetnt catptch sum
        captcha_sum += int(digits [digit_index]);
    print ("sum %d:" %(captcha_sum));

# final check for the last digit
print ("processing index %d, digit %s" %(digit_index + 1, digits[digit_index + 1]));

digit_index += 1
if (digits[digit_index] == digits [0]):
    captcha_sum += int(digits[digit_index]);


print (captcha_sum);