import sys
import utils.inputReaders as ir
import utils.locationHelpers as lh
import math
print("Day 13: Shuttle Search");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

input_data = ir.read_oneline_records_as_list_entries(puzzle_file)

my_time = int(input_data[0])
bus_schedule = input_data[1].split(",")

def nearest_bus_depart_time(time_now,busID):
    depart_time = None
    if isinstance(busID,int):
        time_from_last_dept = time_now%busID
        if time_from_last_dept>0:
            depart_time = time_now + (busID - time_from_last_dept)
        else:
            depart_time = time_now

    return depart_time

nearest_departues = []
for bus in bus_schedule:
    if bus != "x":
        nearest_departues.append( [nearest_bus_depart_time(my_time,int(bus)),int(bus)])

time_table = sorted(nearest_departues,key=lambda x:x[0])
print ("part1: time to wait x bus ID is: %d" %((time_table[0][0]-my_time) * time_table[0][1]))

bus_lines = []
for b in bus_schedule:
    if b != "x":
        bus_lines += [int (b)]


bus_lines = sorted(bus_lines)[::-1]
h_line = bus_lines[0]
offset_from_hline = 0
h_line_pos = bus_schedule.index(str(h_line))

bus_schedule_by_hline = []

bus_lines_from_hline ={}
for b in range(len(bus_schedule)):
    if bus_schedule[b] != "x":
        bus_lines_from_hline[int(bus_schedule[b])]=b - h_line_pos


sec_line = bus_lines[1]
bus_offset = bus_lines_from_hline[sec_line]
ts_sched =[]
t_offs = 0

ts_hl = t_offs

# two buses with longest route set a minimal interval of checking the
# the order. The number will grow later but the base will stay
while len(ts_sched)<2:
    ts_hl += h_line
    exp_dept_time = t_offs + ts_hl + bus_offset
    act_dept_time = nearest_bus_depart_time(exp_dept_time,sec_line)
    if act_dept_time == exp_dept_time:
        ts_sched +=[ts_hl]

ts = ts_sched[1]-ts_sched[0]
t_offs = ts_sched[0]

# departue cycles repeat. The minimal distance worth to check is
# the one when two longest buses meet in given order. Shorter
# routes shoul hit this cycle every n-th time. Looking for n...
t_now = t_offs

t_interval = ts
for b in bus_lines[2:]:
    t_now = t_offs

    ts_sched = []
    bus_offset = bus_lines_from_hline[b]
    print("----bus num %d: start time %d, interval %d" %(b,t_now,t_interval))
    while len(ts_sched)<2:
        t_now += t_interval
        exp_dept_time = t_now + bus_offset
        act_dept_time = nearest_bus_depart_time(exp_dept_time,b)
        if act_dept_time == exp_dept_time:
            ts_sched +=[t_now]
    t_interval = (ts_sched[1] - ts_sched[0])
    t_offs = ts_sched[0]

fbus = int(bus_schedule[0])
print ("part 2: the first occurence of the bus order: %d" %(t_offs +bus_lines_from_hline[fbus]))

