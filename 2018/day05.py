import sys
import re

print("Day 5 puzzle: Alchemical Reduction");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#open file
polymer = ""

with open(puzzle_file, 'r') as puzzle_in:
    polymer = puzzle_in.readline().strip("\n")
puzzle_in.close()

def are_complementary (ch1, ch2):
    if ch1 == "" or ch2 == "":
        return False
    else:
        return abs(ord(ch1) - ord(ch2)) == 32

def is_in_range (index,last_elem):
    return index <= last_elem

def get_unit (index, chain):
    if is_in_range(index, len(chain) -1):
        return chain[index]
    else:
        return ""

def remove_units (unit,polymer):
    return  re.sub (r'[%s]'%unit,"",polymer,flags=re.IGNORECASE)

def reduce_polymer (polymer):
    steady_chain = ""
    i = 0
    boundary = len(polymer)-1
    while is_in_range(i, boundary):
        red = False

        if i == boundary:
            #this is last item, copy
            steady_chain += polymer[i]
            break

        # compare i and i+1 char
        while are_complementary (get_unit(i,polymer),get_unit(i+1,polymer)):
            # reduce
            red = True
            i=i+2

        # check if matches the last from steady
        while are_complementary (get_unit(i,polymer),steady_chain[-1:]):
            steady_chain = steady_chain[:-1]
            red = True
            i += 1

        if not red:
            steady_chain += polymer[i]
            i = i+1
    return steady_chain

print ("The original steady chain is %d units long" %(len(reduce_polymer(polymer))))

units = [chr(x) for x in range(97,123)]

exp_results = []
for u in units:
    exp_results.append([len(reduce_polymer(remove_units(u,polymer))),u])

exp_results = sorted(exp_results)

print ("The best modification is to remove %s unit, the length is %d" %(exp_results[0][1], exp_results[0][0]))
