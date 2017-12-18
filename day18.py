import re;
import sys;

print("Day 18 puzzle: Duet");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

music = [];
pattern = re.compile(r"(\w+)\s(\w+)\s*(.+)*");

#open file
with open(puzzle_file, 'r') as puzzle_in:
    for cur_line in puzzle_in:
        music.append( pattern.match(cur_line.strip("\n")).groups());

puzzle_in.close();


# snd X plays a sound with a frequency equal to the value of X.
# set X Y sets register X to the value of Y.
# add X Y increases register X by the value of Y.
# mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
# mod X Y sets register X to the remainder of dividing the value contained in register X by the value of Y (that is, it sets X to the result of X modulo Y).
# rcv X recovers the frequency of the last sound played, but only when the value of X is not zero. (If it is zero, the command does nothing.)
# jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)

def snd (reg_X, registers):
    # print ("Playing the sound from register %s !" %(reg_X));
    return registers[reg_X];

def set_reg (reg_X, Y, registers):
    # print ("set_reg %s to %d!" %(reg_X, Y));
    registers[reg_X] = Y;
    return ;

def add (reg_X, Y, registers):
    # print ("add %d to reg %s!" %(Y, reg_X));
    registers[reg_X] += Y;
    return ;

def mul (reg_X, Y, registers):
    # print ("mul reg %s by %d!" %(reg_X, Y));
    registers[reg_X] *= Y;
    return ;

def mod (reg_X, Y, registers):
    # print ("mod reg %s by %d!" %(reg_X, Y));
    registers[reg_X] = registers[reg_X] % Y;
    return;

def rcv (reg_X, Y, registers):
    # print ("rcv attepmpt to recover reg %s to %d!" %(reg_X, Y));
    rcv_res = False;
    if registers[reg_X] != 0:
        registers[reg_X] = Y;
        rcv_res = True;
    return rcv_res;

def jgz (cond, Y, registers,ord_index):
    # print ("jgz jumping  by %d if %s!" %(Y, reg_X));
    if cond:
        ord_index += Y;
    else:
        ord_index += 1;
    return ord_index;

registers_0 = {
    "p" : 0
};

registers_1 = {
    "p" : 1
}

registers = {}

track = {
    "set" : set_reg,
    "add" : add,
    "mul" : mul,
    "mod" : mod,
};


# analyse instructions

last_freq = 0;

i = 0;
first_rcv = 0;
queue_0 = [];
queue_1 = [];

reg_X, cmd = "", "";

while i < len(music)  :

    cmd = music[i][0]
    jgz_cond = 0;
    # if we met register name, add entry in registers module
    # print (music[i]);
    if music[i][1].isalpha():
        reg_X = music [i][1];
        if music[i][1] not in registers.keys():
            # print ("arg1 adding key ", music[i][1])
            registers [music[i][1]] = 0;
            # print (registers)

    if cmd == "jgz":
        if music[i][1].isalpha():
            jgz_cond = registers[music[i][1]];
            reg_X = "";
        else:
            jgz_cond = int(music [i][1]);

    # find out values for two arg commands
    val = 0;
    if music[i][2] is not None and music[i][2].isalpha():
        if music[i][2] not in registers.keys():
            # print ("arg2 adding key ", music[i][1])
            registers [music[i][2]] = 0;
            # print (registers)
        val = registers[music[i][2]];
    elif music[i][2] is not None:
        val = int(music[i][2]);

    if cmd == "snd":
        last_freq = snd(reg_X, registers);
        i += 1;
    elif cmd == "rcv":
        if rcv (reg_X, last_freq, registers):
            print ("First rcv command, frequency is: ", last_freq)
            break;
        i += 1;
    elif cmd == "jgz":
        i = jgz(jgz_cond, val, registers,i);
    else:
        track[cmd](reg_X,val,registers);
        i += 1;
    # print (registers);

    # input ("press enter")


