import sys;
import re;

print("Day 16 puzzle: A Series of Tubes");

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
        layout.append(cur_line.strip("\n"));

puzzle_in.close();

x, y = 0, 0;

string = "";

def is_terminator (mark):
    return mark == "+" or mark == " ";

def find_direction (x,y,come_from, layout):
    new_dir = ""
    if come_from  == "up" or come_from == "down" :
        # the possible directions to search are left and right
        if re.match (r'[A-Z,-]', layout[y][x-1]):
            new_dir = "left"
        elif re.match (r'[A-Z,-]', layout[y][x+1]):
            new_dir = "right";
        return new_dir;

    if come_from == "left" or come_from == "right":
        # the possible directions to search are up or down
        if re.match (r'[A-Z,|]', layout[y - 1][x]):
            new_dir = "up"
        elif re.match (r'[A-Z,|]', layout[y + 1][x]):
            new_dir = "down";
        return new_dir;

# try to find the entrance
while x in range(len(layout[y])):
    if layout[y][x] != " ":
        break;
    else:
        x += 1;

if layout[y][x] == '|':
    move_dir = "down";
if layout[y][x] == '-':
    move_dir = "left";

letters = "";
steps = 0;
while True:
    # follow the rabit:
    while not is_terminator(layout[y][x]):
        # verify, we met letter:
        steps += 1;
        if layout[y][x].isalpha():
            letters += layout[y][x];
        if move_dir == "down" :
            y += 1;
        elif move_dir == "up":
            y -= 1;
        elif move_dir == "left":
            x -= 1;
        elif move_dir == "right":
            x += 1;
        # verify, we did not exceeded array
        if y < len(layout) and x < len(layout[0]):
            pass
        else:
            print ("Exceeded array dimension");
            break;

    move_dir = find_direction(x, y, move_dir, layout)
    if move_dir == "down":
        y += 1;
        steps += 1
    elif move_dir == "up":
        y -= 1;
        steps += 1
    elif move_dir == "left":
        x -= 1;
        steps += 1
    elif move_dir == "right":
        x += 1;
        steps +=1;
    else:
        print ("ended at %d %d" %(x, y));
        break;

print ("traceroute is: %s" %(letters));
print ("number of steps is: %d" %(steps));