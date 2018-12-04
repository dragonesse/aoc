import sys
import re
from datetime import datetime

print("Day 4 puzzle: Repose Record");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

# sample form expected on input:
# [1518-11-01 00:05] falls asleep
# year-month-day hour:minute
split_pattern = re.compile(r'^\[(\d+)-(\d+)-(\d+)\s+(\d+):(\d+)\]\s*(.*)$')

#open file
night_events = []

with open(puzzle_file, 'r') as puzzle_in:
    for cur_line in puzzle_in:
        event = re.split(split_pattern,cur_line.strip("\n"))
        event_time = datetime(int(event[1]),int(event[2]),int(event[3]),int(event[4]),int(event[5]))
        event_name = event[6]
        night_events.append([event_time,event_name])

puzzle_in.close()

for event in sorted(night_events):
    print (event[0].isoformat(" "), event[1])
