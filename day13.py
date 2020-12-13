import sys
import utils.inputReaders as ir
import utils.locationHelpers as lh
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

# timestamp = nearest_bus_depart_time(100000000000000,h_line)
print (timestamp)
# for i in range (5):
while (matching_bus_cntr < len(bus_lines)): # or (timestamp <1068788):
    if cntr %1000 == 0:
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

print ("timestamp normalized versus timetable %d" %(timestamp+bus_lines_from_hline[int(bus_schedule[0])]))
