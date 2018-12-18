import sys
import copy

print("Day 18 puzzle: Settlers of The North Pole");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#open file
outskirts = []

with open(puzzle_file, 'r') as puzzle_in:

    for cur_line in puzzle_in:
        outskirts.append(list(cur_line.strip("\n")))
puzzle_in.close()

def print_outskirts (area):
    for i in area:
        print(''.join(i))


def get_neighbours(x,y, area):
    lumberyards = 0
    grounds = 0
    trees = 0
    xstart = x-1 if x > 0 else 0
    xend = x+2 if x < len(area[0]) -1 else x+1

    #top
    if y > 0:
        lumberyards += area[y-1][xstart:xend].count("#")
        grounds += area[y-1][xstart:xend].count('.')
        trees += area[y-1][xstart:xend].count('|')

    #left
    if x>0:
        lumberyards += area[y][x-1].count("#")
        grounds += area[y][x-1].count(".")
        trees += area[y][x-1].count("|")

    #right
    if x<len(area[0])-1:
        lumberyards += area[y][x+1].count("#")
        grounds += area[y][x+1].count(".")
        trees += area[y][x+1].count("|")

    #bottom
    if y < len(area)-1:
        lumberyards += area[y+1][xstart:xend].count("#")
        grounds += area[y+1][xstart:xend].count(".")
        trees += area[y+1][xstart:xend].count("|")

    return [lumberyards,grounds,trees]

def what_next(x,y,area):
    [num_l, num_g, num_t] = get_neighbours(x,y,area)
    type_now = area[y][x]
    type_next = type_now

    if type_now == "." and num_t >= 3:
        type_next = "|"
    elif type_now == "|" and num_l >= 3:
        type_next = "#"
    elif (type_now == "#") and (num_l >= 1 and num_t >= 1):
        type_next = "#"
    elif type_now =="#":
        type_next = "."
    return type_next

def count_resources_factor(area):
    num_lumberyards = 0
    num_woods = 0
    for i in area:
        num_lumberyards += i.count("#")
        num_woods += i.count("|")

    return num_woods * num_lumberyards

outskirts_next = copy.deepcopy(outskirts)
max_time = 1000000000
resources_monitor = [count_resources_factor(outskirts)]
cur_res = 0
minute = 0
repetitions = 5

while resources_monitor.count(cur_res) < repetitions:
    print ("minute %d" %(minute+1))
    minute +=1
    for y in range (len(outskirts)):
        for x in range(len(outskirts[0])):

            if minute%2:
                outskirts_next[y][x] = what_next(x,y,outskirts)
            else:
                outskirts[y][x] = what_next(x,y,outskirts_next)
    if minute%2:
        cur_res = count_resources_factor(outskirts_next)
    else:
        cur_res = count_resources_factor(outskirts)
    resources_monitor.append(cur_res)

first_time_minute = resources_monitor.index(cur_res)
period = (minute - first_time_minute)/(repetitions-1)

periodic_time = max_time - first_time_minute
num_odd_samples = periodic_time%period

print ("the resource value after %d minutes is %d" %(max_time, resources_monitor[first_time_minute+int(num_odd_samples)]))

print ("the resource value after 10 minutes is %d" %(resources_monitor[10]))
