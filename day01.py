import sys
import math

print("Day 1 puzzle: The Tyranny of the Rocket Equation");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];


#open file
loaded_mass = []

with open(puzzle_file, 'r') as puzzle_in:
    loaded_mass = [int(cur_line) for cur_line in puzzle_in]
puzzle_in.close()

# calculate the total fuel
def calculate_fuel (mass):
    return math.floor((mass/3))-2

required_fuel = sum(map(calculate_fuel,loaded_mass))

print ("The rocket requires %d fuel" %(required_fuel))