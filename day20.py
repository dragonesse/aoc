import re;
import sys;
import math;

print("Day 20 puzzle: Particle Swarm");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

def split_coord (vect):
    return list(map(lambda x: int(x), vect.split(",")));


#open file
pattern_vect = re.compile(r'p=<(.+)>,\s+v=<(.+)>,\s+a=<(.*)>');

position = [];
velocity = [];
acceleration = [];

with open(puzzle_file, 'r') as puzzle_in:
    for cur_line in puzzle_in:
        # p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>

        [ pvect,vvect,avect] = pattern_vect.match(cur_line).groups();

        # need to store position as a string to leverage later
        # clist counter and keys
        position.append(pvect);
        velocity.append(split_coord(vvect));
        acceleration.append(split_coord(avect));

puzzle_in.close();

# this is an empiric value of iterations, after which no more collissions appear
for k in range(50):
    print ("===== round %d, num particles %d \n" %(k, len(position)))
    for i in range(len(position)):
        p = split_coord(position[i])
        for axis in range(3):
            # Increase the X velocity by the X acceleration.
            # Increase the Y velocity by the Y acceleration.
            # Increase the Z velocity by the Z acceleration.
            velocity[i][axis] = velocity[i][axis] + acceleration[i][axis]

            # Increase the X position by the X velocity.
            # Increase the Y position by the Y velocity.
            # Increase the Z position by the Z velocity.
            p[axis] = p[axis] + velocity[i][axis]
        # convert the position to a fromat that allows manipulations on the list
        position [i] = ','.join(map(str,p))

    # after all particles moved, it's time to verify whether there are any collisons
    # and remove particles that are in the same position
    freqs = {''.join(i):position.count(i) for i in position}

    for k in freqs.keys():
        if freqs[k] != 1:
            print ("removing %d colliding particles from position " %(freqs[k]), position[position.index(k)])
            for c in range (freqs[k]):
                velocity.pop(position.index(k))
                acceleration.pop(position.index(k))
                position.remove(k)

print ("number of partitions left: %d" %(len(position)))