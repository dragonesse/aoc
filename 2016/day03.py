import re;
print("Day 3 puzzle: Squares With Three Sides");


num_triangles = 0;
sequencer     = 1;
sides = [[0,0,0],[0,0,0],[0,0,0]];
#open file
with open('./puzzle_input/day03.txt', 'r') as puzzle_in:
    for cur_line in puzzle_in:
        print(cur_line.strip("\n"));

        # split string into array of directions
        input_data = re.sub('\s+',' ', cur_line).strip().split(" ");
        # print (input_data);
        sides[0][sequencer%3] = int(input_data[0].strip());
        sides[1][sequencer%3] = int(input_data[1].strip());
        sides[2][sequencer%3] = int(input_data[2].strip());

        # calculate triangle condition:
        if (0 == sequencer%3):
            if ( sides[0][0] + sides[0][1] > sides[0][2] ) and (sides[0][1] + sides[0][2] > sides[0][0]) and (sides[0][2] + sides[0][0] > sides[0][1]):
                num_triangles += 1;
            else:
                print("this is not a triangle %d %d %d" %( sides[0][0], sides[0][1], sides[0][2] ));

            if ( sides[1][0] + sides[1][1] > sides[1][2] ) and (sides[1][1] + sides[1][2] > sides[1][0]) and (sides[1][2] + sides[1][0] > sides[1][1]):
                num_triangles += 1;
            else:
                print("this is not a triangle %d %d %d" %( sides[1][0], sides[1][1], sides[1][2] ));

            if ( sides[2][0] + sides[2][1] > sides[2][2] ) and (sides[2][1] + sides[2][2] > sides[2][0]) and (sides[2][2] + sides[2][0] > sides[2][1]):
                num_triangles += 1;
            else:
                print("this is not a triangle %d %d %d" %( sides[2][0], sides[2][1], sides[2][2] ));
        sequencer += 1;

print ("number of possible trangles is: %d" %num_triangles);
puzzle_in.close();