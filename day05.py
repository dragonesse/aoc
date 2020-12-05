import sys

print("Day 5 puzzle: Binary Boarding");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

board_passes = []

#open file
with open(puzzle_file, 'r') as puzzle_in:
    for cur_line in puzzle_in:
        board_passes.append(cur_line.strip())
puzzle_in.close()


def get_seat_range_by_code(single_code, bound):
    range_half = int(((bound[1] + 1)-bound[0])/2)

    # code for lower half of range
    if single_code in ["F","L"]:
        return [bound[0],bound[1] - range_half]
    # and the upper half
    if single_code in ["B","R"]:
        return [bound[0]+range_half, bound[1]]


def binary_split (code,bound):
    new_bound = get_seat_range_by_code (code[0],bound)
    if len(code)>1:
       approx_pos = binary_split(code[1:],new_bound)
    else:
        # at the very end, the low and high bound will be exactly the same
        # pointing to the location
        return new_bound[0]
    return approx_pos

seats = []
for board_pass in board_passes:
    seat_row = binary_split(board_pass[0:7],[0,127])
    seat_col = binary_split(board_pass[7:],[0,7])
    seats.append(seat_row * 8 + seat_col)

print ("the highest seat id is %d" %(max(seats)))
seats.sort()

for i in range(len(seats)-1):
    if seats[i+1] - seats[i] > 1:
        print ("potential gap between seats %d and %d" %(seats[i] ,seats[i+1]))