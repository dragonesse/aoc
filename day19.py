import sys
print("Day 19 puzzle: Go With The Flow");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#open file
program = []
instr_pointer = 0

with open(puzzle_file, 'r') as puzzle_in:
    blank_matcher = 0
    for cur_line in puzzle_in:
        if "ip" in cur_line:
            instr_pointer = int(cur_line.strip("\n").split(" ")[-1])
        else:
            program.append( cur_line.strip("\n").split(" "))
            program[-1][1:] = [int(x) for x in program[-1][1:]]

puzzle_in.close()
print(program)

# Addition:
# addr (add register) stores into register C the result of adding register A and register B.
# addi (add immediate) stores into register C the result of adding register A and value B.
def addr (regs, cmd):
    regA = regs[cmd[0]]
    regB = regs[cmd[1]]
    regs[cmd[2]] = regA + regB
    return

def addi (regs, cmd):
    regA = regs[cmd[0]]
    valB = cmd[1]
    regs[cmd[2]] = regA + valB
    return

# Multiplication:
# mulr (multiply register) stores into register C the result of multiplying register A and register B.
# muli (multiply immediate) stores into register C the result of multiplying register A and value B.
def mulr (regs, cmd):
    regA = regs[cmd[0]]
    regB = regs[cmd[1]]
    regs[cmd[2]] = regA * regB
    return

def muli (regs, cmd):
    regA = regs[cmd[0]]
    valB = cmd[1]
    regs[cmd[2]] = regA * valB
    return

# Bitwise AND:
# banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
# bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
def banr (regs, cmd):
    regA = regs[cmd[0]]
    regB = regs[cmd[1]]
    regs[cmd[2]] = regA & regB
    return

def bani (regs, cmd):
    regA = regs[cmd[0]]
    valB = cmd[1]
    regs[cmd[2]] = regA & valB
    return

# Bitwise OR:
# borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
# bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
def borr (regs, cmd):
    regA = regs[cmd[0]]
    regB = regs[cmd[1]]
    regs[cmd[2]] = regA | regB
    return

def bori (regs, cmd):
    regA = regs[cmd[0]]
    valB = cmd[1]
    regs[cmd[2]] = regA | valB
    return

# Assignment:
# setr (set register) copies the contents of register A into register C. (Input B is ignored.)
# seti (set immediate) stores value A into register C. (Input B is ignored.)
def setr (regs, cmd):
    regA = regs[cmd[0]]
    regs[cmd[2]] = regA
    return

def seti (regs, cmd):
    valA = cmd[0]
    regs[cmd[2]] = valA
    return

# Greater-than testing:
# gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
# gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
# gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
def gtirr (regs, cmd):
    valA = cmd[0]
    regB = regs[cmd[1]]
    regs[cmd[2]] = 1 if valA > regB else 0
    return

def gtri (regs, cmd):
    regA = regs[cmd[0]]
    valB = cmd[1]
    regs[cmd[2]] = 1 if regA > valB else 0
    return

def gtrr (regs, cmd):
    regA = regs[cmd[0]]
    regB = regs[cmd[1]]
    regs[cmd[2]] = 1 if regA > regB else 0
    return

# Equality testing:
# eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
# eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
# eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
def eqirr (regs, cmd):
    valA = cmd[0]
    regB = regs[cmd[1]]
    regs[cmd[2]] = 1 if valA == regB else 0
    return

def eqri (regs, cmd):
    regA = regs[cmd[0]]
    valB = cmd[1]
    regs[cmd[2]] = 1 if regA == valB else 0
    return

def eqrr (regs, cmd):
    regA = regs[cmd[0]]
    regB = regs[cmd[1]]
    regs[cmd[2]] = 1 if regA == regB else 0
    return

orders = {
    "addi" : addi,
    "addr" : addr,
    "muli" : muli,
    "mulr" : mulr,
    "bori" : bori,
    "borr" : borr,
    "bani" : bani,
    "banr" : banr,
    "gtrr" : gtrr,
    "gtri" : gtri,
    "gtirr" : gtirr,
    "eqri" : eqri,
    "eqrr" : eqrr,
    "eqirr" : eqirr,
    "seti" : seti,
    "setr" : setr
}

def set_ip_reg(reg_id, ip_val, regs):
    regs[reg_id] = ip_val
    return

def get_ip_reg (reg_id, regs):
    return regs[reg_id]

print ("Executing the program")
registers = [0,0,0,0,0,0]
ip_cntr = 0
while ip_cntr < len(program):
    instr = program[ip_cntr]
    set_ip_reg (instr_pointer,ip_cntr,registers)
    print ("ip val: ", ip_cntr, "registers", registers, "instr: ", instr )

    orders[instr[0]](registers,instr[1:])
    ip_cntr = get_ip_reg(instr_pointer,registers)
    ip_cntr += 1
    print ("ip val: ", ip_cntr, "registers", registers )

print("After execution, the registers are:", registers)