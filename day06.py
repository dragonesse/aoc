import sys
import string

print("Day 6 puzzle: Chronal Coordinates");

#read input
puzzle_file = "";
if(len(sys.argv) == 1):
    print ("Please provide input file as argument!");
    sys.exit();
else:
    puzzle_file = sys.argv[1];

#open file
coordinates = []

with open(puzzle_file, 'r') as puzzle_in:

    for cur_line in puzzle_in:
        x = int(cur_line.split(",")[0].strip())
        y = int(cur_line.split(",")[1].strip())
        coordinates.append([x,y])
puzzle_in.close()

print (coordinates)

sorted_by_y = sorted(coordinates, key=lambda x:x[1])
sorted_by_x = sorted(coordinates, key=lambda x:x[0])
[min_y, max_y] = [sorted_by_y[0][1],sorted_by_y[1][1]]
[min_x, max_x] = [sorted_by_x[0][0],sorted_by_x[0][1]]

[top_c,left_c,right_c,down_c] = [sorted_by_y[0],sorted_by_x[0],sorted_by_x[-1],sorted_by_y[-1]]

print ("top left right down", top_c,left_c,right_c,down_c)