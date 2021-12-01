import sys
import utils.inputReaders as ir
import math
print("Day 15: Rambunctious Recitation");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

start_list = ir.read_int_sequence_as_list_entries(puzzle_file,",")

def update_number_history(number, cur_round):
    if number not in num_occurences:
        num_occurences[number] = [cur_round, 0]
    else:
        prev_round = num_occurences[number][1]
        if prev_round != 0:
            num_occurences[number][0] = prev_round
        num_occurences[number][1] = cur_round

num_occurences = {}
for i in range(len(start_list)):
    update_number_history(start_list[i],i+1)

print (num_occurences)
game_end_p1 = 2020
game_end = 30000000
last_num = start_list[-1]
i = len(start_list)

for i in range(len(start_list)+1,game_end+1):

    if num_occurences[last_num][1] !=0:
        last_num = num_occurences[last_num][1] - num_occurences[last_num][0]
    else:
        last_num = 0
    update_number_history(last_num,i)
    if i == game_end_p1:
        print ("part 1: %dth num spoken: %d" %(game_end_p1, last_num))
    i+=1

print ("part 2: %dth num spoken: %d" %(game_end, last_num))

