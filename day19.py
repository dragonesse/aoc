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
        print ("next direction is %s" %(new_dir));
        return new_dir;

    if come_from == "left" or come_from == "right":
        # the possible directions to search are up or down
        if re.match (r'[A-Z,|]', layout[y - 1][x]):
            new_dir = "up"
        elif re.match (r'[A-Z,|]', layout[y + 1][x]):
            new_dir = "down";
        print ("next direction is %s" %(new_dir));
        return new_dir;

def is_end(x,y, come_from, layout):
        is_end = False;
        # the possible directions to search are left and right
        if come_from  == "up":
            if layout[y][x+1] == " " and layout[y][x-1] == " " and layout[y+1][x] == " ":
                is_end = True;
        elif come_from == "down" :
            if layout[y][x+1] == " " and layout[y][x-1] == " " and layout[y-1][x] == " ":
                is_end = True;
        elif come_from == "left" :
            if layout[y+1][x] == " " and layout[y - 1][x] == " " and layout[y][x+1] == " ":
                is_end = True;
        elif come_from == "right" :
            if layout[y+1][x] == " " and layout[y - 1][x] == " " and layout[y][x-1] == " ":
                is_end = True;
        return is_end;

# try to find the entrance
while x in range(len(layout[y])):
    if layout[y][x] != " ":
        break;
    else:
        x += 1;
print ("found entry at %d, %d" %(x,y));

if layout[y][x] == '|':
    move_dir = "down";
if layout[y][x] == '-':
    move_dir = "left";

print ("new direction is %s" %(move_dir));

letters = "";

while True:
    # follow the rabit:
    while not is_terminator(layout[y][x]):
        # verify, we met letter:
        if layout[y][x].isalpha():
            print ("found a letter at %d %d" %(x,y));
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

    print ("marched until %d %d" %(x, y));
    # input ("press enter");

    move_dir = find_direction(x, y, move_dir, layout)
    if move_dir == "down":
        y += 1;
    elif move_dir == "up":
        y -= 1;
    elif move_dir == "left":
        x -= 1;
    elif move_dir == "right":
        x += 1;
    else:
        print ("ended at %d %d" %(x, y));
        break;

print ("traceroute is: %s" %(letters));