import sys

print("Day 5 puzzle: Sunny with a Chance of Asteroids");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#open file
instr_list = []

with open(puzzle_file, 'r') as puzzle_in:
    instr_list = puzzle_in.readline().strip("\n").split(",")
puzzle_in.close()


def parse_modes (modes):
    return list(modes)

def get_value (mode, reg_val):
    return reg_val if mode == 1 else int(instr_list[reg_val])

def parse_instr (instr):
    instr = str(instr).rjust(5,"0")
    return [parse_modes(instr[:-2]) ,instr[-2:]]

# perform addition
def add (val1, val2, position):
    insert_result (val1+val2,position)
    return

def multiply (val1, val2, position):
    insert_result (val1*val2, position)
    return

def save_input (inp, position):
    insert_result(inp, position)
    return

def throw_output (position):
    return instr_list [position]

def insert_result (val, position):
    if position <= len(instr_list):
        instr_list [position] = val
    else:
        print ("Invalid position %d to insert at" %(position))
    return

def modify_input_data(noun=12,verb=2):
    instr_list[1] = noun
    instr_list[2] = verb
    return

def get_val_at_pos (position):
    return instr_list[position] if position <= len (instr_list) else -1

def calc_offset (instr):
    return 4 if is_two_arg_instr(instr) else 2

def is_two_arg_instr (instr):
    return instr in ["01", "02"]

instructions = {
    "01" : add,
    "02" : multiply
    }

pos = 0
test_inp = 1
test_out =[]
while instr_list[pos] != "99":

    [modes , instr] = parse_instr(instr_list[pos])
    print ("position %d, instruction %s %s, arg1 %s" %(pos, ''.join(modes), instr, instr_list[pos+1]))
    v1 = get_value(int(modes[-1]),int(instr_list[pos+1]))
    print ("the value 1: %d" %(v1))
    if is_two_arg_instr(instr):
        v2 = get_value(int(modes[-2]),int(instr_list[pos+2]))
        print ("the value 2: %d the registry: %d" %(v2, int(instr_list[pos+3])))
        instructions[instr](v1,v2,int(instr_list[pos+3]))
    elif instr == "03":
        save_input(test_inp,v1)
    else:
        test_out += [v1]

    offset = calc_offset(instr)
    pos += offset

print (test_out)