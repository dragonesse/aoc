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

#open file
with open(puzzle_file, 'r') as puzzle_in:
    for cur_line in puzzle_in:
        music.append( cur_line.strip("\n"));

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
    if registers[reg_X] != 0:
        registers[reg_X] = Y;
        return True;
    else:
        return False;

def jgz (reg_X, Y, registers,ord_index):
    # print ("jgz jumping  by %d if %s!" %(Y, reg_X));
    if registers[reg_X] > 0:
        ord_index += Y;
    else:
        ord_index += 1;
    return ord_index;

registers = {};

track = {
    "snd" : snd,
    "set" : set_reg,
    "add" : add,
    "mul" : mul,
    "mod" : mod,
    "rcv" : rcv,
    "jgz" : jgz
};


# analyse instructions
pattern = re.compile(r"(\w+)\s(\w+)\s*(.+)*");
last_freq = 0;

i = 0;
first_rcv = 0;
while i < len(music)  :
    # parse the input
    [cmd , reg_X, arg] = pattern.match(music[i]).groups();
    # print (i);
    if reg_X not in registers.keys():
        registers [reg_X] = 0;

    val = 0;
    if arg is not None:
        if arg.isalpha():
            if arg not in registers.keys():
                registers [arg] = 0;
            val = registers[arg];
        else:
            val = int(arg);


    if cmd == "snd":
        last_freq = snd(reg_X, registers);
        i += 1;
    elif cmd == "rcv":
        if rcv (reg_X, last_freq, registers):
            print ("First rcv command, frequency is: ", last_freq)
            break;
        i += 1;
    elif cmd == "jgz":
        i = jgz(reg_X, val, registers,i);
    else:
        track[cmd](reg_X,val,registers);
        i += 1;
    # print (registers);

    # input ("press enter")


