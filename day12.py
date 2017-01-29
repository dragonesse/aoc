import re;
import sys;

print("Day 12 puzzle: Leonardo's Monorail");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

registers = { 'a':0, 'b':0, 'c':0, 'd':0};
commands  = [];

#open file
with open(puzzle_file, 'r') as puzzle_in:
    for cur_line in puzzle_in:
        # print(cur_line.strip("\n"));
        commands.append(cur_line.strip("\n"));
    # print (commands);
puzzle_in.close();

# process commands
cmd_index = 0;
while cmd_index < len(commands):
    # print (commands[cmd_index]);
    cur_cmd = commands [cmd_index];
    # parse the command
    invoke = cur_cmd.split();
    print (invoke);
    if (invoke[0] == "cpy"):
        val_1 = 0;
        # b = a
        # b = int
        if (invoke[1].isalpha()):
            val_1 = registers[invoke[1]];
        else:
            val_1 = int(invoke[1]);

        registers[invoke[2]] = val_1;
        # increment the index
        cmd_index += 1;

    if (invoke[0] == "dec"):
        registers[invoke[1]] -= 1;

        cmd_index += 1;

    if (invoke[0] == "inc"):
        registers[invoke[1]] += 1;
        cmd_index += 1;

    if (invoke [0] == "jnz"):
        val_1, val_2 = 0, 0;
        # check in first arg is non-zero
        if (invoke[1].isalpha()):
            val_1 = registers[invoke[1]];
        else:
            val_1 = int(invoke[1]);

        if (invoke[2].isalpha()):
            val_2 = registers[invoke[2]];
        else:
            val_2 = int(invoke[2]);

        if (val_1 != 0):
            cmd_index += val_2;
        else:
            cmd_index += 1;

print (registers);