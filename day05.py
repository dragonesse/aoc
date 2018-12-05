import sys
import re
from collections import Counter

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

print (polymer)

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

steady_chain = ""
i = 0
boundary = len(polymer)-1
while is_in_range(i, boundary):
    print (i)
    red = False

    if i == boundary:
        #this is last item, copy
        steady_chain += polymer[i]
        break

    # compare i and i+1 char
    while are_complementary (get_unit(i,polymer),get_unit(i+1,polymer)):
        print ("found complementary pair %s-%s" %(get_unit(i,polymer),get_unit(i,polymer)))
        # reduce
        red = True
        i=i+2

    # check if matches the last from steady
    while are_complementary (get_unit(i,polymer),steady_chain[-1:]):
        print ("found complementary pair with stable chain %s-%s" %(get_unit(i,polymer),steady_chain[-1:]))
        steady_chain = steady_chain[:-1]
        red = True
        i += 1

    if not red:
        steady_chain += polymer[i]
        i = i+1

print (steady_chain)
print ("The steady chain is %d units long" %(len(steady_chain)))
