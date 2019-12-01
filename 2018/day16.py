import sys
print("Day 16 puzzle: Chronal Classification");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#open file
init_states =[]
sequence = []
results = []
program = []

with open(puzzle_file, 'r') as puzzle_in:
    blank_matcher = 0
    for cur_line in puzzle_in:
        if "Before" in cur_line:
            init_states.append( [int(x) for x in cur_line.strip("\n").split("[")[-1][:-1].split(",")])
            blank_matcher = 0
        elif "After" in cur_line:
            results.append( [int(x) for x in cur_line.strip("\n").split("[")[-1][:-1].split(",")])
        elif cur_line is not "\n":
            sequence.append( [int(x) for x in cur_line.strip("\n").split(" ")])
        elif cur_line is "\n":
            blank_matcher += 1
        if cur_line is not "\n" and blank_matcher > 1:
            program.append([int(x) for x in cur_line.strip("\n").split(" ")])

puzzle_in.close()

def is_unchanged_except (set1,set2,reg_to_change):
    num_match = 0
    for i in range (4):
        if i != reg_to_change:
            if set1[i] == set2[i]:
                num_match += 1
    return num_match == 3

# Addition:
# addr (add register) stores into register C the result of adding register A and register B.
# addi (add immediate) stores into register C the result of adding register A and value B.
def test_addr (set1, set2, cmd):
    regA = set1[cmd[1]]
    regB = set1[cmd[2]]
    regC = set2[cmd[3]]
    return regA + regB == regC and is_unchanged_except(set1,set2,cmd[3])

def addr (regs, cmd):
    regA = regs[cmd[1]]
    regB = regs[cmd[2]]
    regs[cmd[3]] = regA + regB
    return

def test_addi (set1, set2, cmd):
    regA = set1[cmd[1]]
    valB = cmd[2]
    regC = set2[cmd[3]]
    return regA + valB == regC and is_unchanged_except(set1,set2,cmd[3])

def addi (regs, cmd):
    regA = regs[cmd[1]]
    valB = cmd[2]
    regs[cmd[3]] = regA + valB
    return


# Multiplication:
# mulr (multiply register) stores into register C the result of multiplying register A and register B.
# muli (multiply immediate) stores into register C the result of multiplying register A and value B.
def test_mulr (set1, set2, cmd):
    regA = set1[cmd[1]]
    regB = set1[cmd[2]]
    regC = set2[cmd[3]]
    return regA * regB == regC and is_unchanged_except(set1,set2,cmd[3])

def mulr (regs, cmd):
    regA = regs[cmd[1]]
    regB = regs[cmd[2]]
    regs[cmd[3]] = regA * regB
    return


def test_muli (set1, set2, cmd):
    regA = set1[cmd[1]]
    valB = cmd[2]
    regC = set2[cmd[3]]
    return regA * valB == regC and is_unchanged_except(set1,set2,cmd[3])

def muli (regs, cmd):
    regA = regs[cmd[1]]
    valB = cmd[2]
    regs[cmd[3]] = regA * valB
    return

# Bitwise AND:
# banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
# bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
def test_banr (set1, set2, cmd):
    regA = set1[cmd[1]]
    regB = set1[cmd[2]]
    regC = set2[cmd[3]]
    return regA & regB == regC and is_unchanged_except(set1,set2,cmd[3])

def banr (regs, cmd):
    regA = regs[cmd[1]]
    regB = regs[cmd[2]]
    regs[cmd[3]] = regA & regB
    return

def test_bani (set1, set2, cmd):
    regA = set1[cmd[1]]
    valB = cmd[2]
    regC = set2[cmd[3]]
    return regA & valB == regC and is_unchanged_except(set1,set2,cmd[3])

def bani (regs, cmd):
    regA = regs[cmd[1]]
    valB = cmd[2]
    regs[cmd[3]] = regA & valB
    return

# Bitwise OR:
# borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
# bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
def test_borr (set1, set2, cmd):
    regA = set1[cmd[1]]
    regB = set1[cmd[2]]
    regC = set2[cmd[3]]
    return regA | regB == regC and is_unchanged_except(set1,set2,cmd[3])

def borr (regs, cmd):
    regA = regs[cmd[1]]
    regB = regs[cmd[2]]
    regs[cmd[3]] = regA | regB
    return

def test_bori (set1, set2, cmd):
    regA = set1[cmd[1]]
    valB = cmd[2]
    regC = set2[cmd[3]]
    return regA | valB == regC and is_unchanged_except(set1,set2,cmd[3])

def bori (regs, cmd):
    regA = regs[cmd[1]]
    valB = cmd[2]
    regs[cmd[3]] = regA | valB
    return

# Assignment:
# setr (set register) copies the contents of register A into register C. (Input B is ignored.)
# seti (set immediate) stores value A into register C. (Input B is ignored.)
def test_setr (set1, set2, cmd):
    regA = set1[cmd[1]]
    regC = set2[cmd[3]]
    return regA == regC and is_unchanged_except(set1,set2,cmd[3])

def setr (regs, cmd):
    regA = regs[cmd[1]]
    regs[cmd[3]] = regA
    return


def test_seti (set1, set2, cmd):
    valA = cmd[1]
    regC = set2[cmd[3]]
    return valA == regC and is_unchanged_except(set1,set2,cmd[3])

def seti (regs, cmd):
    valA = cmd[1]
    regs[cmd[3]] = valA
    return

# Greater-than testing:
# gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
# gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
# gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
def test_gtirr (set1, set2, cmd):
    valA = cmd[1]
    regB = set1[cmd[2]]
    regC = set2[cmd[3]]
    return (valA > regB and 1 == regC) or (valA < regB and 0 == regC) and is_unchanged_except(set1,set2,cmd[3])

def gtirr (regs, cmd):
    valA = cmd[1]
    regB = regs[cmd[2]]
    regs[cmd[3]] = 1 if valA > regB else 0
    return

def test_gtri (set1, set2, cmd):
    regA = set1[cmd[1]]
    valB = cmd[2]
    regC = set2[cmd[3]]
    return (regA > valB and 1 == regC) or (regA < valB and 0 == regC) and is_unchanged_except(set1,set2,cmd[3])

def gtri (regs, cmd):
    regA = regs[cmd[1]]
    valB = cmd[2]
    regs[cmd[3]] = 1 if regA > valB else 0
    return

def test_gtrr (set1, set2, cmd):
    regA = set1[cmd[1]]
    regB = set1[cmd[2]]
    regC = set2[cmd[3]]
    return (regA > regB and 1 == regC) or (regA < regB and 0 == regC) and is_unchanged_except(set1,set2,cmd[3])

def gtrr (regs, cmd):
    regA = regs[cmd[1]]
    regB = regs[cmd[2]]
    regs[cmd[3]] = 1 if regA > regB else 0
    return

# Equality testing:
# eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
# eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
# eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
def test_eqirr (set1, set2, cmd):
    valA = cmd[1]
    regB = set1[cmd[2]]
    regC = set2[cmd[3]]
    test_res = False

    return (valA == regB and 1 == regC) or (valA != regB and 0 == regC) and is_unchanged_except(set1,set2,cmd[3])

def eqirr (regs, cmd):
    valA = cmd[1]
    regB = regs[cmd[2]]
    regs[cmd[3]] = 1 if valA == regB else 0
    return

def test_eqri (set1, set2, cmd):
    regA = set1[cmd[1]]
    valB = cmd[2]
    regC = set2[cmd[3]]
    return (regA == valB and 1 == regC) or (regA != valB and 0 == regC) and is_unchanged_except(set1,set2,cmd[3])

def eqri (regs, cmd):
    regA = regs[cmd[1]]
    valB = cmd[2]
    regs[cmd[3]] = 1 if regA == valB else 0
    return

def test_eqrr (set1, set2, cmd):
    regA = set1[cmd[1]]
    regB = set1[cmd[2]]
    regC = set2[cmd[3]]
    return (regA == regB and 1 == regC) or (regA == regB and 0 == regC) and is_unchanged_except(set1,set2,cmd[3])

def eqrr (regs, cmd):
    regA = regs[cmd[1]]
    regB = regs[cmd[2]]
    regs[cmd[3]] = 1 if regA == regB else 0
    return

test_set = {
    "0" : test_addi,
    "1" : test_addr,
    "2" : test_muli,
    "3" : test_mulr,
    "4" : test_bori,
    "5" : test_borr,
    "6" : test_bani,
    "7" : test_banr,
    "8" : test_gtrr,
    "9" : test_gtri,
    "10" : test_gtirr,
    "11" : test_eqri,
    "12" : test_eqrr,
    "13" : test_eqirr,
    "14" : test_seti,
    "15" : test_setr
}

order_mapping={}

num_orders = 16
num_ambiguous = 0
for i in range(len(init_states)):
    num_matches = 0

    for j in range(num_orders):
        order_name = test_set[str(j)].__name__.split("_")[1]
        order_num = str(sequence[i][0])
        if test_set[str(j)](init_states[i],results[i],sequence[i]):
            num_matches +=1
            if order_num in order_mapping.keys():
                if order_name not in order_mapping[order_num]:
                    order_mapping[order_num].append(order_name)
            else:
                order_mapping[order_num] = [order_name]
    if num_matches >= 3:
        num_ambiguous += 1

print ("number of ambiguous commands is %d " %(num_ambiguous))

already_processed = []

elimination = True
while elimination:
    elimination = False
    for k in order_mapping.keys():
        if len(order_mapping[k]) ==1 and order_mapping[k][0] not in already_processed:
            order_name = order_mapping[k][0]
            already_processed.append(order_name)
            elimination = True
            for v in order_mapping.values():
                if order_name in v and len(v)>1:
                    v.remove(order_name)

for k in sorted(order_mapping.keys()):
    order_mapping[k] = ''.join(order_mapping[k])

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
print ("Executing the program")
registers = [0,0,0,0]
for instr in program:
    order_name = order_mapping[str(instr[0])]
    orders[order_name](registers,instr)

print("After execution, the registers are:", registers)