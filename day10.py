import sys
import utils.inputReaders as ir

print("Day 10: Cathode-Ray Tube")

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#read file
the_program = ir.read_oneline_records_as_list_entries(puzzle_file)

cpu_cycle = 1
regx = 1

signal_strength = 0

# 20th, 60th, 100th, 140th, 180th, and 220th
last_check = 220
check_interval = 40

next_check = 20

def read_signal (cycle_num,reg):
    return cycle_num*reg

def is_time(cycle_num,next_check):
    return cycle_num == next_check and next_check <= last_check

def schedule_next_check (cycle_num):
    return cycle_num + check_interval

for instr in the_program:
    # parse
    lval = 0
    if "addx" in instr:
        lval = int(instr.split(' ')[1])
    # process
    if "noop" in instr:
        if is_time(cpu_cycle,next_check):
            signal_strength += read_signal(cpu_cycle,regx)
            next_check = schedule_next_check(cpu_cycle)
        cpu_cycle +=1
    else:
        org_cycle_num = cpu_cycle
        for delta in [0,1,2]:
            if is_time(cpu_cycle + delta,next_check):
                if delta <2:
                    signal_strength += read_signal(cpu_cycle+delta,regx)
                    regx += lval
                elif delta == 2:
                    regx += lval
                    signal_strength += read_signal(cpu_cycle+delta,regx)
                next_check = schedule_next_check(cpu_cycle+delta)
                cpu_cycle += 2
        if org_cycle_num == cpu_cycle:
            cpu_cycle += 2
            regx += lval

print ("Part 1: calculated signal strength is: {}".format(signal_strength))

crt = []
crt_lines = 6
crt_columns = 40

cpu_cycle = 1
regx = 1

for l in range(crt_lines):
    crt.append(["x" for c in range (crt_columns)])

sprite_size =3

def draw(cycle,sprite_pos,crt):
    # get crt line by cycle
    crt_line = (cycle-1)//crt_columns
    beam_pos = (cycle-1)%crt_columns
    if  beam_pos in [sprite_pos-1,sprite_pos,sprite_pos+1]:
        crt[crt_line][beam_pos] = "#"
    else:
        crt[crt_line][beam_pos] = "."
    return

for instr in the_program:
    # parse
    lval = 0
    if "addx" in instr:
        lval = int(instr.split(' ')[1])
    # process
    if "noop" in instr:
        draw(cpu_cycle,regx,crt)
        cpu_cycle +=1
    else:
        draw(cpu_cycle,regx,crt)
        cpu_cycle += 1
        draw (cpu_cycle,regx,crt)
        regx += lval
        cpu_cycle += 1

print("Part 2: The generated image is:")

for l in crt:
    print (''.join(l))
