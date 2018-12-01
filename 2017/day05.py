import re;
import sys;

print("Day 5 puzzle: A Maze of Twisty Trampolines, All Alike");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#open file
step_counter = 0;
stack = [];
with open(puzzle_file, 'r') as puzzle_in:

    stack = [int(line) for line in puzzle_in];

puzzle_in.close();

index = 0;
while (index < len(stack)) and (index >= 0):
    move = stack[index];
    if move >= 3:
        stack[index] -=1;
    else:
        stack[index] += 1;

    index += move;
    step_counter += 1;

print ("Number of instructions: %d" %(step_counter));