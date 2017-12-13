import sys;

print("Day 13 puzzle: Packet Scanners");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

scanners = {};
positions = {};
routes = {};
#open file
with open(puzzle_file, 'r') as puzzle_in:
    for cur_line in puzzle_in:
        [depth, rnge] = cur_line.strip("\n").split(':' );
        scanners[int(depth)] = rnge;
        positions[int(depth)] = [int(depth),0];
        routes [int(depth)] = [x for x in range(int(rnge)-1)]+[x for x in range(int(rnge) - 1,0, -1)];
puzzle_in.close();

print (routes);

def scanner_pos (route, delay):
    # a scanner moves in the loop
    # for range 4 and time of 6 cycles
    # it is present at positions:
    # [layer-n,0]-[layer-n,1]-[layer-n, 2]- [layer-n,3] [layer-n, 2] [layer-n, 1]

    return  route[(delay%len(route))] ;

severity = 0;

ticks   = 0;
pkt_layer = 0

max_layer = max(scanners.keys());

while ticks <= max_layer:
    # clock tick k
    # you move (enter the firewall layer-n)

    pkt_layer = ticks;
    print ("\ntick %d pkt_pos " %(ticks), [pkt_layer,0]);

    # you hit the scanner (or not)
    if pkt_layer in scanners.keys():
        sc_pos = positions[pkt_layer];
        sc_pos = [positions[pkt_layer][0], scanner_pos (routes[pkt_layer],ticks)];
        print ("tick %d sc_pos " %(ticks), sc_pos);


        if not sc_pos[1]:
            print ("layer %d, scanner detected me, what a shame!" %(pkt_layer));
            severity += pkt_layer * int(scanners[pkt_layer]);
        else:
            print ("layer %d, uff, no scanner detected me!" %(pkt_layer));
        positions[pkt_layer] = sc_pos;
    else:
        print ("layer %d is free of scanners!" %(pkt_layer));

    # clock ticks (k+1)
    ticks += 1;
#you move, scanner move, clock ticks



print ("traverse severity is %d" %(severity));



