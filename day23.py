import sys
import int_comp
print("Day 23 puzzle: Category Six")

#read input
puzzle_file = ""
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!")
    sys.exit();
else:
    puzzle_file = sys.argv[1]

#open file
instr_list = []

with open(puzzle_file, 'r') as puzzle_in:
    instr_list = puzzle_in.readline().strip("\n").split(",")
puzzle_in.close()

class NICcomp (int_comp.IntcodeComp):
    def __init__ (self, instr_list, nic_addr):
        super().__init__(instr_list)
        self.packet_list = []
        self.nic_addr = nic_addr
    def add_packet_to_queue (self,packet):
        self.packet_list += [packet]

    def del_packet_from_queue(self):
        del self.packet_list[0]

    def send_packet(self,nicprg):
        nicprg.add_packet_to_queue(self.prog_out[1:])

test_inp = 1
prog = NICcomp(instr_list,5)
prog.add_packet_to_queue([55,66])
prog.add_packet_to_queue([30,76,44][1:])

print (prog.packet_list)

prog.del_packet_from_queue()
print (prog.packet_list)

prog2 = NICcomp(instr_list,7)

prog.prog_out = [1,22,33]
prog.send_packet(prog2)
print (prog2.packet_list)

