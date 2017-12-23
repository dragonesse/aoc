import re;
import sys;

print("Day 23 puzzle: Coprocessor Conflagration");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

orders = [];
pattern = re.compile(r"(\w+)\s(\w+)\s*(.+)*");

#open file
with open(puzzle_file, 'r') as puzzle_in:
    for cur_line in puzzle_in:
        orders.append( pattern.match(cur_line.strip("\n")).groups());

puzzle_in.close();

class Prg:

    def set_reg (self, reg_X, Y):
        self.registers[reg_X] = Y;
        return ;

    def sub (self, reg_X, Y):
        self.registers[reg_X] -= Y;
        return ;

    def mul (self,reg_X, Y):
        self.registers[reg_X] *= Y;
        self.num_mul += 1
        return ;

    def jnz (self,cond, Y, ord_index):
        if cond != 0:
            ord_index += Y;
        else:
            ord_index += 1;
        return ord_index;

    def __init__(self):
        self.registers = {
           "a" : 0,
           "b" : 0,
           "c" : 0,
           "d" : 0,
           "e" : 0,
           "f" : 0,
           "g" : 0,
           "h" : 0,
        }

        self.num_mul = 0;
        self.resumed_at = 0;

        self.track = {
            "set" : self.set_reg,
            "sub" : self.sub,
            "mul" : self.mul,
        }

    # analyse instructions
    def run_prg (self, instructions):
        i = self.resumed_at;

        reg_X, cmd = "", "";

        while i < len(instructions) :

            cmd = instructions[i][0]
            jnz_cond = 0;
            # if we met register name, add entry in registers module
            if instructions[i][1].isalpha():
                reg_X = instructions [i][1];
                if instructions[i][1] not in self.registers.keys():
                    self.registers [instructions[i][1]] = 0;

            if cmd == "jnz":
                if instructions[i][1].isalpha():
                    jnz_cond = self.registers[instructions[i][1]];
                    reg_X = "";
                else:
                    jnz_cond = int(instructions [i][1]);

            val = 0;

            # find out values for two arg commands
            if instructions[i][2] is not None and instructions[i][2].isalpha():
                if instructions[i][2] not in self.registers.keys():
                    self.registers [instructions[i][2]] = 0;
                val = self.registers[instructions[i][2]];
            elif instructions[i][2] is not None:
                val = int(instructions[i][2]);

            if cmd == "jnz":
                i = self.jnz(jnz_cond, val ,i);
            else:
                self.track[cmd](reg_X,val);
                i += 1;
        return 0;

prog = Prg();
prog.run_prg(orders);

print ("prog execute instruction mul %d times" %(prog.num_mul))