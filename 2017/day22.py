import sys;
import time;

print("Day 22 puzzle: Sporifica Virus");

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
    for cur_line in puzzle_in:
        layout.append(list(cur_line.strip("\n")));

puzzle_in.close();


class Cluster:

    @staticmethod
    def position2key (x,y):
        return str(x)+','+str(y)

    def is_infected (self, layout):
        # if the node is infected, the entry exists in dictionary
        return self.position2key(self.x,self.y) in layout

    def get_health_rep (self, layout):
        node_state = None
        # returns state of the node (Infected, Weakened, Flagged)
        if self.position2key(self.x,self.y) in layout:
            node_state = layout[self.position2key(self.x,self.y)]
        return node_state

    def find_direction (self, layout):
        # If it is clean, it turns left.
        # If it is weakened, it does not turn, and will continue moving in the same direction.
        # If it is infected, it turns right.
        # If it is flagged, it reverses direction, and will go back the way it came.

        node_state  = self.get_health_rep(layout)

        if node_state == "W":
            # nothing changes, direction stays the same
            pass
        elif node_state == "I":
            if self.direction  == "up":
                self.direction = "right"
            elif self.direction == "down":
                self.direction = "left";
            elif self.direction == "left":
                self.direction = "up";
            else:
                self.direction = "down"
        # flagged nodes reverse direction
        elif node_state == "F":
            if self.direction  == "up":
                self.direction = "down"
            elif self.direction == "down":
                self.direction = "up"
            elif self.direction == "left":
                self.direction = "right"
            else:
                self.direction = "left"
        else:
            # node apparently is clean
            if self.direction  == "up":
                self.direction = "left"
            elif self.direction == "down":
                self.direction = "right"
            elif self.direction == "left":
                self.direction = "down";
            else:
                self.direction = "up"

        return self.direction;

    def calc_pos (self):
        if self.direction == "up":
            self.y += 1
        elif self.direction == "down":
            self.y -= 1
        elif self.direction == "left":
            self.x -= 1
        elif self.direction == "right":
            self.x += 1
        return self.position2key(self.x,self.y)

    def infect (self,layout):
        if self.position2key(self.x,self.y) in layout:
            layout [self.position2key(self.x,self.y)] = "I"
            self.num_infected += 1
            return 1
        else:
            print ("trying to infect node not present in health map")
            return 0

    def weaken (self, layout):
        if self.position2key(self.x,self.y) not in layout:
            layout [self.position2key(self.x,self.y)] = "W"
            return 1
        else:
            print ("trying to weaken node that is not clean")
            return 0

    def flag (self, layout):
        if self.position2key(self.x,self.y) in layout:
            layout [self.position2key(self.x,self.y)] = "F"
            return 1
        else:
            print ("trying to weaken node that is not in health map")
            return 0

    def heal (self,layout):
        if self.position2key(self.x,self.y) in layout:
            layout.pop(self.position2key(self.x,self.y))
            return 1
        else:
            print ("trying to heal already clean node")
            return 0

    def __init__(self,x, y):
        self.num_infected = 0
        self.x = x
        self.y = -y
        self.direction = "up"
        return

# convert input array to set of infected nodes
infection_map = {}

xinit = len(layout[0])//2
yinit = len(layout)//2
for i in range(len(layout)):
    for j in range(len(layout[0])):
        if layout[i][j] == "#":
            infection_map[Cluster.position2key(j,-i)] = "I"


aoc_cluster = Cluster(xinit,yinit)
num_cycles = 10000000
timestamp = time.time()
for i in range(num_cycles):

    # Setting up new direction, per virus rules (do not move yet)
    aoc_cluster.find_direction(infection_map)

    # Clean nodes become weakened.
    # Weakened nodes become infected.
    # Infected nodes become flagged.
    # Flagged nodes become clean.
    node_health = aoc_cluster.get_health_rep(infection_map)
    if node_health == "W":
        aoc_cluster.infect(infection_map)
    elif node_health == "I":
        aoc_cluster.flag(infection_map)
    elif node_health == "F":
        aoc_cluster.heal(infection_map)
    else:
        aoc_cluster.weaken(infection_map)

    # The virus carrier moves forward one node in the direction it is facing.
    aoc_cluster.calc_pos()


print ("Number of nodes that virus infected is %d" %(aoc_cluster.num_infected))