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

class Prg:

    def snd (self, val_to_snd, r_rcv_q):
        r_rcv_q.append(val_to_snd);
        self.num_send += 1;
        return ;

    def set_reg (self, reg_X, Y):
        self.registers[reg_X] = Y;
        return ;

    def add (self, reg_X, Y):
        self.registers[reg_X] += Y;
        return ;

    def mul (self,reg_X, Y):
        self.registers[reg_X] *= Y;
        return ;

    def mod (self, reg_X, Y):
        self.registers[reg_X] = self.registers[reg_X] % Y;
        return;

    def rcv (self, reg_X):
        rcv_res = False;
        if len(self.receive_q) > 0:
            self.registers[reg_X] = self.receive_q.pop(0);
            rcv_res = True;
        return rcv_res;

    def jgz (self,cond, Y, ord_index):
        if cond > 0:
            ord_index += Y;
        else:
            ord_index += 1;
        return ord_index;

    def __init__(self, prog_id):
        self.registers = {
           "p" : prog_id
        }

        self.prg_id = prog_id;
        self.receive_q = [];
        self.num_send = 0;
        self.resumed_at = 0;

        self.track = {
            "set" : self.set_reg,
            "add" : self.add,
            "mul" : self.mul,
            "mod" : self.mod
        }

    # analyse instructions
    def run_prg (self, r_rcv_q, instructions):
        i = self.resumed_at;

        reg_X, cmd = "", "";

        while i < len(instructions) :

            cmd = instructions[i][0]
            jgz_cond = 0;
            # if we met register name, add entry in registers module
            if instructions[i][1].isalpha():
                reg_X = instructions [i][1];
                if instructions[i][1] not in self.registers.keys():
                    self.registers [instructions[i][1]] = 0;

            if cmd == "jgz":
                if instructions[i][1].isalpha():
                    jgz_cond = self.registers[instructions[i][1]];
                    reg_X = "";
                else:
                    jgz_cond = int(instructions [i][1]);

            val = 0;
            if cmd == "snd":
                if instructions[i][1].isalpha():
                    val = self.registers[instructions[i][1]];
                    reg_X = "";
                else:
                    val = int(instructions [i][1])

            # find out values for two arg commands
            if instructions[i][2] is not None and instructions[i][2].isalpha():
                if instructions[i][2] not in self.registers.keys():
                    self.registers [instructions[i][2]] = 0;
                val = self.registers[instructions[i][2]];
            elif instructions[i][2] is not None:
                val = int(instructions[i][2]);

            if cmd == "snd":
                self.snd(val, r_rcv_q);
                i += 1;
            elif cmd == "rcv":
                if self.rcv (reg_X):
                    i += 1;
                else:
                    # we need to stop execution, but need to keep track where we stopped
                    self.resumed_at = i;
                    return i;
            elif cmd == "jgz":
                i = self.jgz(jgz_cond, val ,i);
            else:
                self.track[cmd](reg_X,val);
                i += 1;
        return 0;

deadlock = False;

pr0 = Prg(0);
pr1 = Prg(1);

while not deadlock:

    # run prog 0 as far as possible
    pr0.run_prg( pr1.receive_q, music);
    # run prog 1 as far as possible
    pr1.run_prg( pr0.receive_q, music);

    # programs stop at rcv commands
    # if both queues are empty, we have a deadlock
    if len(pr0.receive_q) == 0 and len(pr1.receive_q) == 0:
        deadlock = True;

print ("prog 1 send %d messages" %(pr1.num_send))