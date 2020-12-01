import sys
import re

print("Day 4 puzzle: Secure Container");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#open file
range_low, range_end = 0, 0

with open(puzzle_file, 'r') as puzzle_in:
    [range_low, range_end] = (int(r) for r in puzzle_in.readline().strip("\n").split("-"))
puzzle_in.close()

def generate_next_part(part):
    return list(range(int(str(part)[-1]),10))

def extend_part (part):
    new_parts = [str(part)+str(n) for n in generate_next_part(part)]
    if len(str(part)) < 6:
        tmp = []
        for t in [extend_part(np) for np in new_parts]:
            tmp += t
        new_parts = tmp

    return new_parts

def has_repeating_digits(entry):
    return len(re.findall(r"(?=([1-9])\1)", entry)) > 0

def fits_restricted_pattern(entry):

    for d in entry:
        if entry.count(d)==2:
            return True
    return False

possible_codes = extend_part(0)

print ("num generated codes: ",len(possible_codes))

code_cntr = 0
code_cntr_rest = 0

for code in possible_codes:
    if (int(code) >= range_low) and (int(code)<=range_end):
        if has_repeating_digits(code):
            code_cntr +=1
        if fits_restricted_pattern(code):
            code_cntr_rest +=1


print ("num codes that fit: ", code_cntr)
print ("num restricted codes that fit: ", code_cntr_rest)


