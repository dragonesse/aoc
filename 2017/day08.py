import re;
import sys;

print("Day 8 puzzle: I Heard You Like Registers");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

def isequal (arg1, arg2):
    return arg1 == arg2;

def isnequal (arg1, arg2):
    return arg1 != arg2;

def isgrtr (arg1, arg2):
    return arg1 > arg2;

def isgrtreq (arg1, arg2):
    return arg1 >= arg2;

def issmlr (arg1, arg2):
    return arg1 < arg2;

def issmlreq (arg1, arg2):
    return arg1 <= arg2;

def incr (reg,amount):
    return reg + amount;

def decr (reg, amount):
    return reg - amount;

operations = {
    "==" : isequal,
    "!=" : isnequal,
    ">"  : isgrtr,
    "<"  : issmlr,
    ">=" : isgrtreq,
    "<=" : issmlreq
};

commands = {
    "inc" : incr,
    "dec" : decr
};

#open file

registers = {};
highest_val = 0;
with open(puzzle_file, 'r') as puzzle_in:
    for cur_line in puzzle_in:
        # parse register, condition and operation
        [wreg,oper,val,ifst,creg,coper,cval] = cur_line.strip("\n").split();

        # if register does not exists, add it to hash
        for key in [wreg,creg]:
            if key not in registers:
                registers[key] = 0;

        if operations[coper](registers[creg],int(cval)):
            #execute operation on register
            registers[wreg] = commands[oper](registers[wreg],int(val));
            if registers[wreg] > highest_val:
                highest_val = registers[wreg];

puzzle_in.close();

print ("max end value is: %d" %(max(registers.values())));
print ("max value ever is: %d" %(highest_val));