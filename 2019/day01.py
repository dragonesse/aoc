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
    fuel= math.floor((mass/3))-2
    return fuel if fuel > 0 else 0
tot_fuel_per_unit =[]

for unit_num in range(len(loaded_mass)):
    mass = loaded_mass[unit_num]

    fuel = calculate_fuel (mass)
    tot_fuel_per_unit += [fuel]
    while fuel > 0:
        mass = fuel
        fuel = calculate_fuel (mass)
        tot_fuel_per_unit[unit_num] += fuel

    tot_fuel_per_unit[unit_num] += fuel

required_fuel = sum(map(calculate_fuel,loaded_mass))
print ("The rocket requires %d fuel for part 1" %(required_fuel))

required_fuel = sum(tot_fuel_per_unit)
print ("The rocket requires %d fuel for part 2" %(required_fuel))