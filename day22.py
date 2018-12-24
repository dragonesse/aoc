import sys
print("Day 22 puzzle: Mode Maze")

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!")
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#open file
depth =0
target = []
# depth: 510
# target: 10,10
with open(puzzle_file, 'r') as puzzle_in:
    for cur_line in puzzle_in:
        if "depth" in cur_line:
            depth = int(cur_line.strip("\n").split(" ")[1])
        elif "target" in cur_line:
            target= [int(x) for x in cur_line.strip("\n").split(" ")[1].split(",")]

puzzle_in.close()

print (depth,target)

cave_map = []
for i in range(target[1]+1):
    cave_map.append([0]*(target[0]+1))
# print (cave_map)

def calc_geo_index(x,y,cave_map):
    gi = 0
    if x == 0 and y == 0:
        gi =0
    elif (x == len(cave_map[0]) -1) and (y == len(cave_map) -1):
        print("reached target")
        gi = 0
    elif x == 0:
        gi = y * 48271
    elif y == 0:
        gi = x * 16807
    else:
        gi = cave_map [y][x-1] * cave_map[y-1][x]

    return gi

def calc_erosion_lvl(x,y,depth, cave_map):
    el = (calc_geo_index(x,y,cave_map) + depth) % 20183

    # if y==len(cave_map):
    #     cave_map.append([0]*len(cave_map[0]))
    cave_map[y][x] = el
    # print(cave_map)
    return el

def calc_geo_type(er_lvl):
    gt = er_lvl % 3
    sym = ""
    if gt == 0:
        # print ("rocky")
        sym = "."
    if gt == 1:
        # print ("wet")
        sym = "="
    if gt == 2 :
        # print ("narrow")
        sym = "|"
    return sym

def calc_risk_lvl(er_lvl):
    return er_lvl%3

risk_lvl = 0
for y in range(target[1]+1):
    for x in range(target[0]+1):
        # print (x,y)
        risk_lvl += calc_risk_lvl(calc_erosion_lvl(x,y,depth,cave_map))

    # print(''.join([calc_geo_type(el) for el in cave_map[y]]))
print ("the global risk level is %d" %(risk_lvl))

