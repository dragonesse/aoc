import sys
print("Day 19 puzzle: Go With The Flow");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#open file
program = []
instr_pointer = 0

with open(puzzle_file, 'r') as puzzle_in:
    blank_matcher = 0
    for cur_line in puzzle_in:
        if "ip" in cur_line:
            instr_pointer = int(cur_line.strip("\n").split(" ")[-1])
        else:
            program.append( cur_line.strip("\n").split(" "))
            program[-1][1:] = [int(x) for x in program[-1][1:]]

puzzle_in.close()

print ("Executing the program")
bignum = 10551288
facsum = 0

for i in range (1, bignum+1):
    if bignum%i == 0:
        facsum +=i

print ("After execution, the sum of factors is: %d" %(facsum))