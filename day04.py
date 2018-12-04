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
split_pattern_event = re.compile(r'^\[(\d+)-(\d+)-(\d+)\s+(\d+):(\d+)\]\s*(.*)$')
split_pattern_guard = re.compile (r'Guard #(\d+)')
#open file
night_events = []
guard_ids = []
with open(puzzle_file, 'r') as puzzle_in:
    for cur_line in puzzle_in:
        event = re.split(split_pattern_event,cur_line.strip("\n"))

        event_time = datetime(int(event[1]),int(event[2]),int(event[3]),int(event[4]),int(event[5]))
        event_name = event[6]
        night_events.append([event_time,event_name])
        guard_id = re.split(split_pattern_guard,event_name)
        if len(guard_id) == 3 and (guard_id[1] not in guard_ids):
            guard_ids.append(guard_id[1])
puzzle_in.close()

night_events = sorted(night_events)

# for event in night_events:
#     print (event[0].isoformat(" "), event[1])

print (guard_ids)

guard_watch = {}

for guard in guard_ids:
    guard_watch[guard] = [0 for _ in range(60)]
    for log_index in range(len(night_events)):
        if guard in night_events[log_index][1]:
            print ("guard # %s begins shift" %(guard))
            while "falls" in night_events[log_index + 1][1] :
                print ("found guard %s sleepy" %(guard))
                start_sleep = night_events[log_index + 1][0].time().minute
                stop_sleep = night_events[log_index + 2][0].time().minute
                print ("sleep time from %d to %d" %(start_sleep,stop_sleep))
                for minute in range (start_sleep,stop_sleep):
                    guard_watch[guard][minute] += 1
                log_index += 2
                print (log_index, len(night_events))
                if log_index >= len(night_events)-1:
                    print("hit end of the list")
                    break

# for g in guard_watch.items():
#     print (g)

# by now, there should be a map with guard ID and its sleeping schedule
# find most sleepy guy
sleeper = [0,0]
for guard in guard_watch.keys():
    sleep_time = sum(guard_watch[guard])
    if sleep_time > sleeper[1]:
        print ("have new sleepy id: %s minutes: %d" %(guard,sleep_time))
        sleeper[0] = int(guard)
        sleeper[1] = sleep_time

# choose the most probable minute
most_hits = max(guard_watch[str(sleeper[0])])
most_likely_sleep = guard_watch[str(sleeper[0])].index(most_hits)
print ("The winner is guard %d who slept %d minutes, %d" %(sleeper[0],sleeper[1],sleeper[0]*most_likely_sleep))

