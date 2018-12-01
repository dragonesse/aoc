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
routes = {};
#open file
with open(puzzle_file, 'r') as puzzle_in:
    for cur_line in puzzle_in:
        [depth, rnge] = cur_line.strip("\n").split(':' );
        scanners[int(depth)] = rnge;
        routes [int(depth)] = [x for x in range(int(rnge)-1)]+[x for x in range(int(rnge) - 1,0, -1)];
puzzle_in.close();

def scanner_pos (route, delay):
    # a scanner moves in the loop
    # for range 4 and time of 6 cycles
    # it is present at positions:
    # [layer-n,0]-[layer-n,1]-[layer-n, 2]- [layer-n,3] [layer-n, 2] [layer-n, 1]
    return route[ delay%len(route)]

max_layer = max(scanners.keys());
lucky_layers = 0;

delay = 9;
while lucky_layers != len(scanners):
    # scanners move, pkt not (yet)
    delay += 1

    pkt_layer = 0
    lucky_layers = 0;

    # clock tick k
    # you move (enter the firewall layer-n)
    while pkt_layer <= max_layer:

        # verify if you hit the scanner (or not)
        if pkt_layer in scanners.keys():
            sc_pos = scanner_pos (routes[pkt_layer],(delay+pkt_layer));

            if not sc_pos:
                print ("layer %d scanner detected me, what a shame!" %(pkt_layer));
                break;

            else:
                lucky_layers += 1

        # clock ticks (k+1), pkt move to next layer
        pkt_layer += 1;

print ("packet passed undetected with delay of %d" %(delay));