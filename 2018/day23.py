import sys
import re
import math
print("Day 23 puzzle: Experimental Emergency Teleportation");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#open file
nanorobots =[]
# pos=<0,0,0>, r=4
pattern =  re.compile(r'^.*\<(\-*[0-9]+),(\-*[0-9]+),(\-*[0-9]+).*=([0-9]+)$')
with open(puzzle_file, 'r') as puzzle_in:
    for cur_line in puzzle_in:
        nanorobots.append( (list(int(x) for x in re.match(pattern,cur_line).group(1,2,3,4))) )

puzzle_in.close()
strongest_bot = max(nanorobots,key = lambda x:x[3])
max_radius = strongest_bot[3]
print(max_radius)

def cab_distance (spoint,epoint=[0,0,0]):
    return abs(epoint[0]-spoint[0])+abs(epoint[1]-spoint[1])+abs(epoint[2]-spoint[2])

# for i in range(len(nanorobots) ):
#     nanorobots[i].append(cab_distance(nanorobots[i],[0,0,0]))


# for i in sorted(nanorobots,key = lambda x:x[3],reverse=True):
#     print (i)

# for i in nanorobots:
#     if cab_distance(i,[0,0,0])<=i[3]:
#         print ("0,0,0 is in range of ", i)


# print ("mid val x: ", sorted(nanorobots, key=lambda x:x[0])[498:501])
# print ("mid val y: ", sorted(nanorobots ,key=lambda x:x[1])[498:501])
# print ("mid val z: ", sorted(nanorobots, key=lambda x:x[2])[498:501])

# print ("min-max x: ", min(nanorobots, key=lambda x:x[0]), max(nanorobots, key=lambda x:x[0]))
# print ("min-max y: ", min(nanorobots, key=lambda x:x[1]), max(nanorobots, key=lambda x:x[1]))
# print ("min-max z: ", min(nanorobots, key=lambda x:x[2]), max(nanorobots, key=lambda x:x[2]))

# for i in nanorobots:
#     print (i)


# num_in_range = 0
# for i in nanorobots:
#     dist = cab_distance(i,best_pos)
#     if dist <= i[3]:
#         print ("best pos is in range of: ",i[0:3], ", the distance is %d" %(dist))
#         num_in_range +=1
#     else:
#         print ("best pos is not in range", i[0:3], ", the distance is %d" %(dist))
#         pass
# print ("the number of nanobots in range of strongest signal is: %d" %(num_in_range))


mid_point = round(len(nanorobots)/2)
sum([x[0] for x in sorted(nanorobots, key=lambda x:x[0])[2:4]])/2

midx = round(sum([x[0] for x in sorted(nanorobots, key=lambda x:x[0])[mid_point-1:mid_point+1]] )/2)
midy = round(sum([y[1] for y in sorted(nanorobots, key=lambda x:x[1])[mid_point-1:mid_point+1]])/2)
midz = round(sum([z[2] for z in sorted(nanorobots, key=lambda x:x[2])[mid_point-1:mid_point+1]])/2)

step = round(min (nanorobots,key=lambda x:x[3])[3]/2)

minx = min(nanorobots, key=lambda x:x[0])
maxx = max(nanorobots, key=lambda x:x[0])
miny = min(nanorobots, key=lambda x:x[1])
maxy = max(nanorobots, key=lambda x:x[1])
minz = min(nanorobots, key=lambda x:x[2])
maxz = max(nanorobots, key=lambda x:x[2])

start_point = [midx,midy,midz]

print(start_point)

def generate_surrounding(point, jump):
    s = [[point [0],point[1],point[2]]]
    s.append([x+jump for x in point])
    s.append([point[0] + jump, point[1], point[2]])
    s.append([point[0], point[1] + jump, point[2]])
    s.append([point[0], point[1], point[2] + jump])
    s.append([point[0] + jump, point[1] + jump, point[2]])
    s.append([point[0] + jump, point[1], point[2] + jump])
    s.append([point[0], point[1] + jump, point[2] + jump])
    s.append([x-jump for x in point])
    s.append([point[0] - jump, point[1], point[2]])
    s.append([point[0], point[1] - jump, point[2]])
    s.append([point[0], point[1], point[2] - jump])
    s.append([point[0] - jump, point[1] - jump, point[2]])
    s.append([point[0] - jump, point[1], point[2] - jump])
    s.append([point[0], point[1] - jump, point[2] - jump])
    # print(s)
    return s


teleport=[]
num_in_range = 0
max_in_range = -1
new_val = True
new_dist = True
jump = step
empty_checks = 0
ec_max = 10
while new_val or new_dist or step > 1:
    new_val = False
    new_dist = False
    print ("generate new surrounding")
    surrounding = generate_surrounding(start_point,jump)

    for s in surrounding:
        num_in_range = 0
        for p in nanorobots:
            if cab_distance(p,s) <= p[3]:
                num_in_range +=1

        # print ("numer nanobots in range ",s,": %d" %(num_in_range))
        if num_in_range > max_in_range:
            print ("found new teleport, with %d nanobots in range, dist from you %d" %(num_in_range,cab_distance(s)))
            teleport = [s[0],s[1],s[2]]
            max_in_range = num_in_range
            new_val = True
        elif num_in_range == max_in_range:
            if cab_distance(teleport)>cab_distance(s):
                print("found a point closer to you, the distance is: %d" %(cab_distance(s)))
                teleport = [s[0],s[1],s[2]]
                new_dist = True
    if not new_val or not new_dist:
        empty_checks +=1

    if empty_checks < ec_max:
        jump += jump
    else:
        if new_val:
            start_point = [teleport[0],teleport[1],teleport[2]]
        # elif new_dist and not new_dist:

        step = round(step/2)
        print("select new start_point, change step to %d" %(step))
        empty_checks = 0
        jump = step
        if step<50:
            ec_max = 20

cd = cab_distance(teleport,[0,0,0])
print (teleport,cd)
print(cd > 77852209)
