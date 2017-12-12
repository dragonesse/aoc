import math;
import sys;

print("Day 12 puzzle: Digital Plumber");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

pipes = {};

#open file
with open(puzzle_file, 'r') as puzzle_in:
    for cur_line in puzzle_in:
        [src, dst] = cur_line.strip("\n").split('<->' );
        pipes[int(src)] = [ int(x) for x in dst.split(',')];

puzzle_in.close();

print (pipes);

# analyse stream and track current child position
visited = set();

# for a given key, make values a new keys and read new values

dest = pipes [0];
next_dest = pipes.copy();

visited.add(0);
app_cntr = 1; # zero connects to itsetf

# print ("\ndestinations: ",dest);

i = 0;
# while i < 7:
while next_dest:

    next_dest = [];

    for prog in dest:
        print ("checking program %d" %(prog));
        if prog not in visited:
            print ("looking at connections of new program");
            for candidate in pipes[prog]:
                if candidate not in visited:
                    print ("adding new candidate %d" %(candidate));
                    next_dest = next_dest + [candidate] ;
                    print (next_dest);
            app_cntr += 1;
            visited.add(prog);
    dest = next_dest.copy();
    i += 1;
    print ("next programs to check", next_dest);

print ("number of programs that communicate with prog0 is %d" %(app_cntr));



