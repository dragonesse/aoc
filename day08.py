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

mem = memory_state()

while not visited_instr[mem.code_index]:
    instr = program_code[mem.code_index][0]
    val = int(program_code[mem.code_index][1])
    visited_instr[mem.code_index] = True
    instructions[instr](val,mem)

print ("part 1: accumulator value: %d" %mem.global_acc)