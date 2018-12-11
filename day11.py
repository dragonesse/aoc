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

def calc_power_level (x,y,grid_no):
    rack_ID = get_rack_ID(x)
    power_lvl = (rack_ID*y + grid_no)*rack_ID
    return get_hundrets(power_lvl) - 5

def get_hundrets (num):
    return int(str(num)[-3])

print(calc_power_level(3,5,8))
print(calc_power_level(122,79,57))
print(calc_power_level(217,196,39))
print(calc_power_level(101,153,71))