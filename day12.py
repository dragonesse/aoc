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

# analyse stream and track current child position
visited = set();

app_cntr = 0;
grp_cntr = 0;

# looking for groups
for src in pipes.keys():
    if src not in visited:
        print ("checking starting group search for prog %d" %(src));
        dest = pipes [src];
        next_dest = dest.copy();
        visited.add(src);
        app_cntr = 1; # group parent connects to itsetf
        grp_cntr += 1;

        while next_dest:
            next_dest = [];

            # for a given program (key), check its connections (values)
            # if they they are connecting with some entity not checked yet

            for prog in dest:
                if prog not in visited:
                    for candidate in pipes[prog]:
                        if candidate not in visited:
                            next_dest = next_dest + [candidate] ;
                    app_cntr += 1;
                    visited.add(prog);
            dest = next_dest.copy();
        print ("number of programs that communicate with prog%d is %d" %(src,app_cntr));
    else:
        next_dest = [];

print ("number of groups is %d" %(grp_cntr));



