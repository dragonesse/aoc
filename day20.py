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
    # list(map((lambda x: x + 100), casualties))
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

        position.append(split_coord(pvect));
        velocity.append(split_coord(vvect));
        acceleration.append(split_coord(avect));

puzzle_in.close();

min_dist = sys.maxsize;
particle    = 0;
distance = [0] * len(position)
# for i in range(len(position)):
#     distance[i] += sum(list(map((lambda x: math.fabs(x)), position[i])))

# this is an arbitratry value, the algorithm shall compare for how long
# the new winner stays on position and stop when new winner will
# stay longer than previous one
for k in range(330):
    print ("===== round %d \n" %(k))
    for i in range(len(position)):
        # print   (position[i], velocity[i],acceleration[i]);
        # d = distance[i]
        # print ("distance before: %d" %(distance[i]))
        for axis in range(3):
            # Increase the X velocity by the X acceleration.
            # Increase the Y velocity by the Y acceleration.
            # Increase the Z velocity by the Z acceleration.
            velocity[i][axis] = velocity[i][axis] + acceleration[i][axis]

            # Increase the X position by the X velocity.
            # Increase the Y position by the Y velocity.
            # Increase the Z position by the Z velocity.
            position[i][axis] = position[i][axis] + velocity[i][axis]
        distance[i] = math.fabs(position[i][0]) + math.fabs(position[i][1]) + math.fabs(position[i][2])
    print (distance.index(min(distance)))
    if particle != distance.index(min(distance)):
        particle = distance.index(min(distance))
        k += 1;
    else:
        print ("the particle %d won again! Iteration %d" %(particle,k))
        # break;

        # print ("after calculations: ", position[i])
        # calculate distance from <0,0,0>
# for i in range(len(position)):
    # distance[i] = sum(list(map((lambda x: math.fabs(x)), position[i])))

    # print ("the distance of particle id %d after is %d" %(i , distance[i]));


print ("the partcile %d was closest to 0.0.0" %(distance.index(min(distance))))