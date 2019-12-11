import sys
import int_comp
print("Day 9 puzzle: Sensor Boost");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#open file
instr_list = []

with open(puzzle_file, 'r') as puzzle_in:
    instr_list = puzzle_in.readline().strip("\n").split(",")
puzzle_in.close()


test_inp = 1
prog = int_comp.IntcodeComp(instr_list)
prog_res = prog.exec_prog(test_inp)

print ("tests results for part 1:", prog_res)

test_inp = 2
prog = int_comp.IntcodeComp(instr_list)
prog_res = prog.exec_prog(test_inp)

print ("tests results for part 2:", prog_res)