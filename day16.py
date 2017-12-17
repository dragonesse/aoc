import sys;

print("Day 16 puzzle: Permutation Promenade");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

layout = [];

#open file
with open(puzzle_file, 'r') as puzzle_in:
    layout = puzzle_in.read().strip("\n").split(",");

puzzle_in.close();

def spin (num_places, order):
    order = order[-num_places:]+order[:-num_places];
    return order;

def exchange (pos_a, pos_b, order):
    tmp = order[pos_a];
    order [pos_a] = order [pos_b];
    order [pos_b] = tmp
    return order;

def partner (prog_a, prog_b, order):
    a_pos = order.index(prog_a);
    b_pos = order.index(prog_b);
    return  exchange (a_pos, b_pos, order);

def decode_move (instruction):
    return instruction[0];

def decode_args (name, instruction):
    if name == "s":
        arg1 = int(instruction[1:]);
        return arg1;
    elif name == "p":
        [arg1, arg2] = instruction[1:].split('/');
        return [arg1,arg2];
    else:
        [arg1, arg2] = instruction[1:].split('/');
        return [int(arg1),int(arg2)];

moves = {
    "s" : spin,
    "x" : exchange,
    "p" : partner,
};

dancers = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p'];

# analyse stream and track current child position
num_iters = 1000000000;
first_dance = "";
i = 0;
while i < num_iters:
    if not i%1000000:
        print ("%d mln elapsed, %d to go" %(i, num_iters - i))
    for step in layout:
        sname = decode_move (step);

        # dance
        if sname == "s":
            dancers = moves[sname](decode_args(sname,step),dancers);
        else:
            sarg = decode_args(sname,step);
            dancers = moves[sname](sarg[0],sarg[1],dancers);

    if i == 0:
        first_dance = dancers.copy();
    elif dancers == first_dance:
        print ("after %d iterations the pattern repeats" %(i+1));
        print (dancers);
        # we need to calculate only remainder
        i = num_iters - (num_iters % (i))
        print ("increasing counter to %d" %(i));
    i += 1;

print ("final position is ", ''.join(dancers));
