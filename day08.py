import sys

print("Day 8 puzzle: Handheld Halting");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#open file
program_code = []

with open(puzzle_file, 'r') as puzzle_in:
    for cur_line in puzzle_in:
        program_code.append(cur_line.strip().split(' '))

puzzle_in.close()


visited_instr = [False for i in range(len(program_code))]

class memory_state:
    def __init__(self):
        self.global_acc = 0
        self.code_index = 0


def upd_acc (val,mem):
    mem.global_acc += val
    upd_index(1,mem)

def upd_index(val,mem):
    mem.code_index += val

def do_nop(val,mem):
    upd_index(1,mem)

instructions ={
    "acc" : upd_acc,
    "jmp" : upd_index,
    "nop" : do_nop
}

def clear_memory(mem):
    mem.global_acc = 0
    mem.code_index = 0

def clear_path ():
    return [False for i in range(len(program_code))]

def load_code(pc):
    return pc.copy()

mem = memory_state()

while not visited_instr[mem.code_index]:
    instr = program_code[mem.code_index][0]
    val = int(program_code[mem.code_index][1])
    visited_instr[mem.code_index] = True
    instructions[instr](val,mem)

print ("part 1: accumulator value: %d" %mem.global_acc)

subs_list = []

for i in range(len(program_code)):
    if program_code[i][0] in ["jmp","nop"]:
        subs_list += [i]

for inst_ind in subs_list:
    clear_memory(mem)
    visited_instr = clear_path()
    upd_code = program_code
    org_inst = ""
    if program_code[inst_ind][0] == "jmp":
        upd_code[inst_ind][0] = "nop"
        org_inst = "jmp"
    else:
        upd_code[inst_ind][0] = "jmp"
        org_inst ="nop"


    while (not visited_instr[mem.code_index]):
        instr = upd_code[mem.code_index][0]
        val = int(upd_code[mem.code_index][1])

        visited_instr[mem.code_index] = True
        instructions[instr](val,mem)

        if (mem.code_index ==len(upd_code)):
            print ("seems you reached the last line")
            print("part 2: code index: %d acc val: %d" %(mem.code_index,mem.global_acc))
            break
    # program_code and updated_code share the same reference, so
    # a cleanup is needed here
    program_code[inst_ind][0] = org_inst
