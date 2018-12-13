import sys
import copy

print("Day 13 puzzle: Mine Cart Madness");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#open file
tracks =[]
carts = []

with open(puzzle_file, 'r') as puzzle_in:

    for cur_line in puzzle_in:
        tracks.append (list(cur_line.strip("\n")))
puzzle_in.close()

[print (''.join(tracks[i])) for i in range(len(tracks))]

class Cart:
    def __init__(self, x, y, direction=""):
        self.x = x
        self.y = y
        self.direction = direction
        self.intersec_cntr = 0

    def __lt__(self,other):
        if self.y == other.y:
            return self.x < other.x
        if self.x == other.x:
            return self.y < other.y
        if self.x != other.x:
            return self.y < other.y


    def __eq__ (self,other):
        return self.x == other.x and self.y == other.y

    def turn_left(self):
        print ("Turning left")
        if self.direction == ">":
            self.direction = "^"

        elif self.direction == "<":
            self.direction = "v"

        elif self.direction == "v":
            self.direction = ">"

        else:
            self.direction = "<"
        return

    def turn_right(self):
        print ("Turning right")
        if self.direction == ">":
            self.direction = "v"

        elif self.direction == "<":
            self.direction = "^"

        elif self.direction == "v":
            self.direction = "<"

        else:
            self.direction = ">"
        return

    def go_straight(self):
        print ("Going straight")
        if self.direction == ">":
            self.x += 1

        elif self.direction == "<":
            self.x -= 1

        elif self.direction == "v":
            self.y += 1

        elif self.direction == "^":
            self.y -= 1
        return

    def handle_intersection(self):
        print ("------Met an intersection")
        if self.intersec_cntr%3 == 0:
            self.turn_left()
        # elif self.intersec_cntr%3 == 1:
        #     self.go_straight()
        elif self.intersec_cntr%3 == 2:
            self.turn_right()
        self.intersec_cntr += 1
        return

    def handle_curve (self, c_type):
        print ("------Met a curve")
        if c_type == '/':
            if self.direction == "^" or self.direction == "v" :
                self.turn_right()
            elif self.direction == ">" or self.direction == "<":
                self.turn_left()

        elif c_type == '\\':
            if self.direction == "^" or self.direction == "v" :
                self.turn_left()
            elif self.direction == ">" or self.direction == "<":
                self.turn_right()
        return

    def get_cur_pos (self):
        return [self.x, self.y]

    def make_next_move (self, track_ahead):
        # if track_ahead == "-" or track_ahead == "|":
        #     pass
        if track_ahead == "\\" or track_ahead == "/":
            self.handle_curve(track_ahead)
        elif track_ahead == "+":
            self.handle_intersection()

        self.go_straight()
        return

    def print_coordinates (self):
        print ("x, y: [%d, %d] direction: %s" % (self.x, self.y, self.direction))
        return

def is_a_cart (track_piece):
    if track_piece == ">" or track_piece == "<" or track_piece == "^" or track_piece == "v":
        return True
    else:
        return False

def fill_track(track_piece):
    if track_piece == ">" or track_piece == "<":
        return "-"
    elif track_piece == "^" or track_piece == "v":
        return "|"

active_cars = []
# read cars from the track map
for i in range(len(tracks)):
    for j in range (len(tracks[0])):
        track_piece = tracks[i][j]
        if is_a_cart(track_piece):
            active_cars.append(Cart(j,i,track_piece))
            active_cars[-1].print_coordinates()
            tracks[i][j] = fill_track(track_piece)

# cur_cars = copy.deepcopy(active_cars)
# active_cars[3].go_straight()
# active_cars[4].go_straight()

# for i in range(len(cur_cars)):
#     print ("\n")
#     cur_cars[i].print_coordinates()
#     active_cars[i].print_coordinates()

# active_cars.remove(Cart(1,0,">"))

# print ("delete")
# for i in range(len(active_cars)):
#     # print ("\n")
#     # cur_cars[i].print_coordinates()
#     active_cars[i].print_coordinates()


# sys.exit()
# move on
collison = False
tick = 0
while len(active_cars) > 1:
    print ("------starting tick %d " %(tick))
    future_pos = []
    # cur_cars = copy.deepcopy(active_cars)
    for i in sorted(active_cars):
        print ("\n")
        i.print_coordinates()
        cur_pos = i.get_cur_pos()
        road_ahead = tracks[cur_pos[1]][cur_pos[0]]
        i.make_next_move(road_ahead)
        i.print_coordinates()
        cur_pos = i.get_cur_pos()
        if cur_pos in future_pos:
            print ("found collison, the coordinates are ", i.get_cur_pos())
            # active_cars.remove(Cart(1,0,">"))
            active_cars.remove(Cart(cur_pos[0],cur_pos[1],""))
            active_cars.remove(Cart(cur_pos[0],cur_pos[1],""))
            future_pos.remove([cur_pos[0],cur_pos[1]])
            # collison = True
            # break

        else:
            future_pos.append(i.get_cur_pos())
    tick += 1

print ("the last car left: ")
active_cars[0].print_coordinates()