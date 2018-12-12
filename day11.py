import sys

print("Day 11 puzzle: Chronal Charge")

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!")
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#open file
grid_serial_no = 0

with open(puzzle_file, 'r') as puzzle_in:

    grid_serial_no = int(puzzle_in.readline().strip("\n"))

puzzle_in.close()

x_start,y_start = 1,1
x_end,y_end = 300, 300

def get_rack_ID (x):
    return x+10

def calc_cell_power (x,y,grid_no):
    rack_ID = get_rack_ID(x)
    power_lvl = (rack_ID*y + grid_no)*rack_ID
    return get_hundrets(power_lvl) - 5

def get_hundrets (num):
    return int(str(num)[-3])

def calc_block_power(xtop,ytop,grid_no,block_size):
    power = 0
    for xoffs in range(block_size):
        for yoffs in range (block_size):
            power += calc_cell_power(xtop  +xoffs, ytop + yoffs,grid_no)
    return power

max_block_size = 300
max_power = 0
block_top = [-1,-1]
square_size = 0
# grid_serial_no = 18

#this iterates from 1 to 299
for block_size in range(1, max_block_size):
    for x in range (x_end - block_size):
        for y in range (y_end - block_size):
            pwr = calc_block_power(x+1, y+1, grid_serial_no, block_size)
            if pwr > max_power:
                max_power = pwr
                block_top = [x+1,y+1]
                square_size = block_size

# handle 300x300 case
pwr = calc_block_power(x_start,y_start,grid_serial_no, max_block_size)
if pwr > max_power:
    max_power = pwr
    block_top = [x_start,y_start]
    square_size = max_block_size


print ("The biggest power block begins at: ", block_top, "size: %d, level %d" %(square_size,max_power))