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

with open(puzzle_file, 'r') as puzzle_in:

    for cur_line in puzzle_in:
        if "Before" in cur_line:
            init_states.append( [int(x) for x in cur_line.strip("\n").split("[")[-1][:-1].split(",")])
        elif "After" in cur_line:
            results.append( [int(x) for x in cur_line.strip("\n").split("[")[-1][:-1].split(",")])
        elif cur_line is not "\n":
            sequence.append( [int(x) for x in cur_line.strip("\n").split(" ")])
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
    print ("testing addr")
    regA = set1[cmd[1]]
    regB = set1[cmd[2]]
    regC = set2[cmd[3]]
    return regA + regB == regC and is_unchanged_except(set1,set2,cmd[3])

def test_addi (set1, set2, cmd):
    print ("testing addi")
    regA = set1[cmd[1]]
    valB = cmd[2]
    regC = set2[cmd[3]]
    return regA + valB == regC and is_unchanged_except(set1,set2,cmd[3])

# Multiplication:
# mulr (multiply register) stores into register C the result of multiplying register A and register B.
# muli (multiply immediate) stores into register C the result of multiplying register A and value B.
def test_mulr (set1, set2, cmd):
    print ("testing mulr")
    regA = set1[cmd[1]]
    regB = set1[cmd[2]]
    regC = set2[cmd[3]]
    return regA * regB == regC and is_unchanged_except(set1,set2,cmd[3])

def test_muli (set1, set2, cmd):
    print ("testing muli")
    regA = set1[cmd[1]]
    valB = cmd[2]
    regC = set2[cmd[3]]
    return regA * valB == regC and is_unchanged_except(set1,set2,cmd[3])

# Bitwise AND:
# banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
# bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
def test_banr (set1, set2, cmd):
    print ("testing banr")
    regA = set1[cmd[1]]
    regB = set1[cmd[2]]
    regC = set2[cmd[3]]
    return regA & regB == regC and is_unchanged_except(set1,set2,cmd[3])

def test_bani (set1, set2, cmd):
    print ("testing bani")
    regA = set1[cmd[1]]
    valB = cmd[2]
    regC = set2[cmd[3]]
    return regA & valB == regC and is_unchanged_except(set1,set2,cmd[3])


# Bitwise OR:
# borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
# bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
def test_borr (set1, set2, cmd):
    print ("testing borr")
    regA = set1[cmd[1]]
    regB = set1[cmd[2]]
    regC = set2[cmd[3]]
    return regA | regB == regC and is_unchanged_except(set1,set2,cmd[3])

def test_bori (set1, set2, cmd):
    print ("testing bori")
    regA = set1[cmd[1]]
    valB = cmd[2]
    regC = set2[cmd[3]]
    return regA | valB == regC and is_unchanged_except(set1,set2,cmd[3])

# Assignment:
# setr (set register) copies the contents of register A into register C. (Input B is ignored.)
# seti (set immediate) stores value A into register C. (Input B is ignored.)
def test_setr (set1, set2, cmd):
    print ("testing setr")
    regA = set1[cmd[1]]
    regC = set2[cmd[3]]
    return regA == regC and is_unchanged_except(set1,set2,cmd[3])

def test_seti (set1, set2, cmd):
    print ("testing seti")
    valA = cmd[1]
    regC = set2[cmd[3]]
    return valA == regC and is_unchanged_except(set1,set2,cmd[3])


# Greater-than testing:
# gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
# gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
# gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
def test_gtirr (set1, set2, cmd):
    print ("testing gtirr")
    valA = cmd[1]
    regB = set1[cmd[2]]
    regC = set2[cmd[3]]
    return (valA > regB and 1 == regC) or (valA < regB and 0 == regC) and is_unchanged_except(set1,set2,cmd[3])

def test_gtri (set1, set2, cmd):
    print ("testing gtri")
    regA = set1[cmd[1]]
    valB = cmd[2]
    regC = set2[cmd[3]]
    return (regA > valB and 1 == regC) or (regA < valB and 0 == regC) and is_unchanged_except(set1,set2,cmd[3])

def test_gtrr (set1, set2, cmd):
    print ("testing gtrr")
    regA = set1[cmd[1]]
    regB = set1[cmd[2]]
    regC = set2[cmd[3]]
    return (regA > regB and 1 == regC) or (regA < regB and 0 == regC) and is_unchanged_except(set1,set2,cmd[3])

# Equality testing:
# eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
# eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
# eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
def test_eqirr (set1, set2, cmd):
    print ("testing equirr")
    valA = cmd[1]
    regB = set1[cmd[2]]
    regC = set2[cmd[3]]
    test_res = False

    return (valA == regB and 1 == regC) or (valA != regB and 0 == regC) and is_unchanged_except(set1,set2,cmd[3])

def test_eqri (set1, set2, cmd):
    print ("testing eqri")
    regA = set1[cmd[1]]
    valB = cmd[2]
    regC = set2[cmd[3]]
    return (regA == valB and 1 == regC) or (regA != valB and 0 == regC) and is_unchanged_except(set1,set2,cmd[3])

def test_eqrr (set1, set2, cmd):
    print ("testing eqrr")
    regA = set1[cmd[1]]
    regB = set1[cmd[2]]
    regC = set2[cmd[3]]
    return (regA == regB and 1 == regC) or (regA == regB and 0 == regC) and is_unchanged_except(set1,set2,cmd[3])

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

num_orders = 16
num_ambiguous = 0
for i in range(len(init_states)):
    num_matches = 0
    for j in range(num_orders):
        print ("init state: ", init_states[i])
        print ("result : ", results[i])
        print ("command: ", sequence[i])
        if test_set[str(j)](init_states[i],results[i],sequence[i]):
            num_matches +=1
        if num_matches >= 3:
            num_ambiguous += 1
            break

print ("number of ambiguous commands is %d " %(num_ambiguous))