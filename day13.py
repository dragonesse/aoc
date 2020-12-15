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

print (nearest_departues)
time_table = sorted(nearest_departues,key=lambda x:x[0])
print ("the nearest bus is at: ", time_table[0] )
print ("time to wait is: %d" %((time_table[0][0]-my_time) * time_table[0][1]))

bus_lines = []
for b in bus_schedule:
    if b != "x":
        bus_lines += [int (b)]


bus_lines = sorted(bus_lines)[::-1]
h_line = bus_lines[0]
offset_from_hline = 0
h_line_pos = bus_schedule.index(str(h_line))

print ("highest bus ID: %d" %h_line)
# print(bus_schedule)
# print (h_line_pos)
bus_schedule_by_hline = []

bus_lines_from_hline ={}
for b in range(len(bus_schedule)):
    if bus_schedule[b] != "x":
        bus_lines_from_hline[int(bus_schedule[b])]=b - h_line_pos

print(bus_lines_from_hline)

matching_bus_cntr = 1
timestamp = 1068785 - (3*h_line)
cntr = int(timestamp/h_line)
timestamp = h_line
cntr = 1

if len(bus_schedule) > 6:
    timestamp = nearest_bus_depart_time(100000000000000,h_line) - int(3*h_line)
    cntr = int(timestamp/h_line)
    print (timestamp,cntr)
# sys.exit()
# for i in range (5):
if False:
    while (matching_bus_cntr < len(bus_lines)): # or (timestamp <1068788):
        if cntr %10000 == 0:
            print ("==== evaluating timestamp %d" %timestamp)
        for bus_num in bus_lines[1:]:
            # print ("evaluating bus %d " %bus_num)
            bus_offset_from_hline = bus_lines_from_hline[bus_num]
            exp_dept_time = timestamp+bus_offset_from_hline
            act_dept_time = nearest_bus_depart_time(exp_dept_time,bus_num)
            # print ("expected time %d actual time %d diff %d" %(exp_dept_time,act_dept_time, exp_dept_time - act_dept_time))

            if act_dept_time == exp_dept_time:
                # print ("bus %d matches the schedule" %bus_num)
                matching_bus_cntr += 1
            else:
                # print( "at least one bus does not fit the schedule")
                matching_bus_cntr = 1
                cntr +=1
                timestamp = cntr*h_line
                break
        # print ("%d buses matching for timestamp %d" %(matching_bus_cntr, timestamp))

    print ("part 1: timestamp normalized versus timetable %d" %(timestamp+bus_lines_from_hline[int(bus_schedule[0])]))

sec_line = bus_lines[1]


sec_line = bus_lines[1]
bus_offset = bus_lines_from_hline[sec_line]
ts_sched =[]
t_offs = 0

if len(bus_schedule) > 6:
    aoc_hint = 99999999456533
    t_offs = nearest_bus_depart_time(aoc_hint,h_line) - int(5*h_line)
    cntr = int(timestamp/h_line)
    print (timestamp,cntr)
# sys.exit()
ts_hl = t_offs

while len(ts_sched)<2:
    ts_hl += h_line
    exp_dept_time = t_offs + ts_hl + bus_offset
    act_dept_time = nearest_bus_depart_time(exp_dept_time,sec_line)
    if act_dept_time == exp_dept_time:
        print ("at ts: %d two longest buses come in order" %ts_hl)
        ts_sched +=[ts_hl]



fcntr = 0
i = 0
ts = ts_sched[1]-ts_sched[0]
t_offs = ts_sched[0]
cts = 0
print ("time offset: %d, time diff between departs: %d " %(t_offs,ts))

# sys.exit()

while (fcntr)<len(bus_lines):
    i +=1
    cts = t_offs + (i*ts)
    if i%100000 == 0:
        print ("======evaluating timestamp for hline: %d" %(cts) )

    for j in bus_lines :
        bus_offset_from_hline = bus_lines_from_hline [j]
        exp_dept_time = cts+bus_offset_from_hline
        act_dept_time = nearest_bus_depart_time(exp_dept_time,j)
        # print ("bus num: ",j, ":", act_dept_time)

        if act_dept_time == exp_dept_time:
            fcntr +=1
        else:
            # print ("order not kept, for bus %d the diff is %d" %(j, exp_dept_time-act_dept_time))
            fcntr =0
            break


print ("current timestamp for hline: %d" %(cts) )
fbus = int(bus_schedule[0])
print("part 2 the earliest bus is: ",nearest_bus_depart_time(cts+bus_lines_from_hline[fbus],fbus) )