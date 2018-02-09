import re;
import sys;
print("Day 24 puzzle: Electromagnetic Moat");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];


#open file
connectors = {};
with open(puzzle_file, 'r') as puzzle_in:
    for cur_line in puzzle_in:
        # the format of input:
        #0/43
        connectors[cur_line.strip("\n")] = 0 # the value is not in use

puzzle_in.close();


class Bridge_constructor:
    def __init__ (self, warehouse):
        self.warehouse = warehouse
        self.gangways = {}
        self.bridge = "0/0"

    def find_next_span (self,pin):
        pattern_con1 = re.compile(r'^'+pin+'/([\d]+)$');
        pattern_con2 = re.compile(r'^([\d]+)/'+pin+'$');

        spans = []
        for c in self.warehouse.keys():
            # detect if connector matches our needs but also is not used yet
            if ((pattern_con1.match(c) != None) or (pattern_con2.match(c) != None)) and (self.warehouse [c] == 0):
                spans.append(c)

        return spans

    def free_pin (self,span, pin):
        pattern_con1 = re.compile(r'^'+pin+'/([\d]+)$');
        pattern_con2 = re.compile(r'^([\d]+)/'+pin+'$');

        free_pin = None;

        if pattern_con1.match(span):
            free_pin = pattern_con1.match(span).groups()[0]
        else:
            free_pin = pattern_con2.match(span).groups()[0]
        return free_pin

    def build_bridge (self,pin,bridge):
        for s in self.find_next_span(pin):
            # block span
            self.warehouse[s] = 1
            cur_bridge = bridge + "--" + s
            self.gangways[cur_bridge] = cur_bridge.count("/")
            next_pin = self.free_pin(s, pin)
            self.build_bridge (next_pin,cur_bridge)
            # release the span for future use
            self.warehouse[s] = 0;
        return

way_over_moat = Bridge_constructor(connectors)

way_over_moat.build_bridge("0", "0/0")
print ("total num of bridges: ", len(way_over_moat.gangways))
strongest = 0
for g in way_over_moat.gangways.keys():
    g_strenght = sum(list(map(lambda x: int(x), g.replace("--","/").split("/"))))
    if g_strenght > strongest:
        strongest = g_strenght
print ("The strongest gangway is: ", strongest)

# find how long is the longest gangway
max_num_spans = max(way_over_moat.gangways.values())
# find all gangways of this length
longest_bridges = [k for k, v in way_over_moat.gangways.items() if v == max_num_spans]

strongest = 0
for g in longest_bridges:
    g_strenght = sum(list(map(lambda x: int(x), g.replace("--","/").split("/"))))
    if g_strenght > strongest:
        strongest = g_strenght

print ("The strongest over longest is: ", strongest)
