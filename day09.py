import sys

print("Day 9 puzzle: Sensor Boost");

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

    try:
        if mode == 1:
            return reg_val
        elif mode == 0:
            return int(instr_list[reg_val])
        else:
            return int(instr_list[reg_val+relative_base])
    except IndexError:
        print ("out of memory access, no cell at address %d returning zero" %(reg_val+relative_base))
        return 0

def parse_instr (instr):
    instr = str(instr).rjust(5,"0")
    return [parse_modes(instr[:-2]) ,instr[-2:]]

def add (val1, val2, position):
    insert_result (val1+val2,position)
    return

def multiply (val1, val2, position):
    insert_result (val1*val2, position)
    return

def less_than (val1, val2, position):
    insert_result (int(val1<val2),position)
    return

def equals (val1, val2, position):
    insert_result (int(val1 == val2),position)
    return

def jump_if_true (val1,val2,pointer):
    return val2 if val1 != 0 else pointer

def jump_if_false (val1,val2,pointer):
    return val2 if val1 == 0 else pointer

def save_input (inp, position,mode):
    if mode == 2:
        insert_result(inp, position+relative_base)
    else:
        insert_result(inp, position )
    return

def insert_result (val, position, instr_list = instr_list):
    if position < len(instr_list):
        instr_list [position] = val
    else:
        for i in range(position - len(instr_list)):
            instr_list += [0]
        instr_list += [val]
    return


def get_val_at_pos (position):
    return instr_list[position] if position <= len (instr_list) else -1

def calc_pos_for_insert (position,mode):

    if mode == 2:
        return position+relative_base
    elif mode == 0:
        return position
    else:
        print ("invalid mode for insert operation")
        raise ValueError

def calc_offset (instr):
    if is_three_arg_instr(instr):
        return 4
    elif is_two_arg_instr (instr):
        return 3
    else:
        return 2

def is_three_arg_instr (instr):
    return instr in instructions.keys()

def is_two_arg_instr (instr):
    return instr in orders.keys()

instructions = {
    "01" : add,
    "02" : multiply,
    "07" : less_than,
    "08" : equals
    }

orders ={
    "05" : jump_if_true,
    "06" : jump_if_false
}

relative_base = 0
pos = 0
test_inp = 2
test_out =[]
while instr_list[pos] != "99":
    set_offset = True

    [modes , instr] = parse_instr(instr_list[pos])

    v1 = get_value(int(modes[-1]),int(instr_list[pos+1]))
    if is_three_arg_instr(instr):
        v2 = get_value(int(modes[-2]),int(instr_list[pos+2]))
        ins_pos = calc_pos_for_insert(int(instr_list[pos+3]),int(modes[-3]))
        instructions[instr](v1,v2,ins_pos)
    elif is_two_arg_instr(instr):
        v2 = get_value(int(modes[-2]),int(instr_list[pos+2]))
        next_pos = orders[instr](v1,v2,pos)
        if next_pos != pos:
            pos = next_pos
            set_offset = False
    elif instr == "03":
        v1 = int(instr_list[pos+1])
        save_input(test_inp,v1,int(modes[-1]))
    elif instr == "09":
        relative_base += v1
    else:
        test_out += [v1]

    if set_offset:
        offset = calc_offset(instr)
        pos += offset

print ("tests results: ",test_out)