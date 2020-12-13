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
bus_lines = input_data[1].split(",")

def nearest_bus_depart_time(time_now,busID):
    depart_time = None
    if isinstance(busID,int):
        time_from_last_dept = time_now%busID
        depart_time = time_now + (busID - time_from_last_dept)

    return depart_time

nearest_departues = []
for bus in bus_lines:
    if bus != "x":
        nearest_departues.append( [nearest_bus_depart_time(my_time,int(bus)),int(bus)])

print (nearest_departues)
time_table = sorted(nearest_departues,key=lambda x:x[0])
print ("the nearest bus is at: ", time_table[0] )
print ("time to wait is: %d" %((time_table[0][0]-my_time) * time_table[0][1]))

