import sys;
import re;

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
        return Cluster.position2key(self.x,self.y) in layout

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

        # node_infected = self.is_infected (layout)
        node_state  = self.get_health_rep(layout)
        # print ("find_direction: node is infected ", node_infected)

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

        # if self.direction  == "up":
        #     if node_infected:
        #         self.direction = "right"
        #     else:
        #         self.direction = "left"
        # elif self.direction == "down":
        #     if node_infected:
        #         self.direction = "left";
        #     else:
        #         self.direction = "right"
        # elif self.direction == "left":
        #     if node_infected:
        #         self.direction = "up";
        #     else:
        #         self.direction = "down";
        # elif self.direction == "right":
        #     if node_infected:
        #         self.direction = "down";
        #     else:
        #         self.direction = "up";

        # print ("find_direction: new direction is %s" %(self.direction))
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
        # print ("calc_pos: new pos is: %d %d" %(self.x, self.y))
        return self.position2key(self.x,self.y)

    def infect (self,layout):
        if self.position2key(self.x,self.y) not in layout:
            layout [self.position2key(self.x,self.y)] = "I"
            self.num_infected += 1
            return 1
        else:
            print ("trying to infect existing node")
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

# convert map to set of infected nodes
infection_map = {}

xinit = len(layout[0])//2
yinit = len(layout)//2
for i in range(len(layout)):
    for j in range(len(layout[0])):
        if layout[i][j] == "#":
            infection_map[Cluster.position2key(j,-i)] = "I"


aoc_cluster = Cluster(xinit,yinit)
num_cycles = 10000
for i in range(num_cycles):
    # If the current node is infected, it turns to its right. Otherwise, it turns to its left.
    # (Turning is done in-place; the current node does not change.)
    aoc_cluster.find_direction(infection_map)

    # If the current node is clean, it becomes infected. Otherwise, it becomes cleaned. (This is done after the node is considered for the purposes of changing direction.)
    if aoc_cluster.is_infected(infection_map):
        aoc_cluster.heal(infection_map)
    else:
        aoc_cluster.infect(infection_map)

    # The virus carrier moves forward one node in the direction it is facing.
    aoc_cluster.calc_pos()

print ("number of nodes that virus infected is %d" %(aoc_cluster.num_infected))