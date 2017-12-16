import math;
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
    print ("spin: ", num_places)
    order = order[-num_places:]+order[:-num_places];
    print (order);
    return order;

def exchange (pos_a, pos_b, order):
    print ("exchange: ", pos_a, pos_b);
    tmp = order[pos_a];
    order [pos_a] = order [pos_b];
    order [pos_b] = tmp
    print (order);
    return order;

def partner (prog_a, prog_b, order):
    print ("partner", prog_a, prog_b);
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
        # print("decode_args for p: ", instruction[1:].split('/'))
        [arg1, arg2] = instruction[1:].split('/');
        return [arg1,arg2];
    else:
        # print("decode_args for x: ", instruction[1:].split('/'))
        [arg1, arg2] = instruction[1:].split('/');
        return [int(arg1),int(arg2)];

moves = {
    "s" : spin,
    "x" : exchange,
    "p" : partner,
};

dancers = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"];

# dancers = ["a","b","c","d","e"];

# analyse stream and track current child position


for step in layout:
    print(step);
    sname = decode_move (step);

    # dance
    print (dancers);
    if sname == "s":
        dancers = moves[sname](decode_args(sname,step),dancers);
    else:
        sarg = decode_args(sname,step);
        dancers = moves[sname](sarg[0],sarg[1],dancers);

    # input ("press enter");

print ("final position is ", ''.join(dancers));

# print ("total distance is: %d" %( calc_dist(start_x, start_y)) );
# print ("max distance is: %d" %( max_dist) );
