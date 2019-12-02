import sys

print("Day 2 puzzle: T1202 Program Alarm");

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
    instr_list = [int(instr) for instr in puzzle_in.readline().strip("\n").split(",")]
puzzle_in.close()

print (instr_list)

# perform addition
def add (val1, val2, position):
    print ("add of %d, %d. Result stored on pos %d" %(val1,val2,position))
    insert_result (val1+val2,position)
    return

def multiply (val1, val2, position):
    print ("mul of %d, %d. Result stored on pos %d" %(val1,val2,position))
    insert_result (val1*val2, position)
    return

def insert_result (val, position):
    if position <= len(instr_list):
        instr_list [position] = val
    else:
        print ("Invalid position %d to insert at" %(position))
    return

def modify_input_data():
    instr_list[1] = 12
    instr_list[2] = 2

def get_val_at_pos (position):
    return instr_list[position] if position <= len (instr_list) else -1

instructions = {
    "1" : add,
    "2" : multiply
    }

pos = 0
offset = 4
modify_input_data()
while instr_list[pos] != 99:

    instructions[str(instr_list[pos])](get_val_at_pos(instr_list[pos+1]),get_val_at_pos(instr_list[pos+2]),instr_list[pos+3])
    print (instr_list)
    pos += offset