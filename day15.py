import sys;

print("Day 15 puzzle: Dueling Generators");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];


#open file
gen_a_seed, gen_b_seed = 0, 0;
with open(puzzle_file, 'r') as puzzle_in:
    for cur_line in puzzle_in:
        [gen_a_seed, gen_b_seed] = [int(x) for x in (cur_line).strip("\n").split(",")];

puzzle_in.close();

def is_equal(val1, val2):

    bitmask = 0xFFFF;
    if (val1 & bitmask) == (val2 & bitmask):
        return True;
    else:
        return False;

def generate (prev_val, factor):
    div = 2147483647;
    return (prev_val*factor)%div;


gen_a_factor = 16807;
gen_b_factor = 48271;

gen_a_val = gen_a_seed;
gen_b_val = gen_b_seed;

judge_cntr = 0;


for i in range (int(40E6)):
    if not i%100E3:
        print ("iteration %d, matches %d" %(i, judge_cntr));
    gen_a_val = generate(gen_a_val, gen_a_factor);
    gen_b_val = generate(gen_b_val, gen_b_factor);

    if is_equal(gen_a_val,gen_b_val):
        judge_cntr += 1;

print("numer of matching pairs %d" %(judge_cntr));