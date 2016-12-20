import math;

print("Day 1 puzzle: Bathroom security");

#open file
# pin_pad = [[1,2,3],[4,5,6],[7,8,9]];
pin_pad = [["0","0","1","0","0"],["0","2","3","4","0"],["5","6","7","8","9"],["0","A","B","C","0"],["0","0","D","0","0"]];

print (pin_pad[0]);
print (pin_pad[1]);
print (pin_pad[2]);

finger_pos  = [2,0];
passcode    = "";
with open('./puzzle_input/day02.txt', 'r') as puzzle_in:
    for cur_line in puzzle_in:
        print(cur_line.strip("\n"));

        # split string into array of directions
        directions = cur_line.strip("\n");
        # calculate actual move
        for move in directions:

            if ( "U" == move ) and (finger_pos [0] > 0) and (pin_pad[finger_pos[0]-1][finger_pos[1]] != "0"):
                finger_pos [0] -= 1;
                print ("move U %s:" %( pin_pad[finger_pos[0]][finger_pos[1]] ));

            elif ("D" == move) and (finger_pos [0] < 4) and (pin_pad[finger_pos[0]+1][finger_pos[1]] != "0"):
                finger_pos [0] += 1;
                print ("move D %s:" %( pin_pad[finger_pos[0]][finger_pos[1]] ));
            elif ("R" == move) and (finger_pos [1] < 4) and (pin_pad[finger_pos[0]][finger_pos[1]+1] != "0"):
                finger_pos [1] += 1;
                print ("move R %s:" %( pin_pad[finger_pos[0]][finger_pos[1]] ));
            elif ("L" == move) and (finger_pos [1] > 0) and (pin_pad[finger_pos[0]][finger_pos[1]-1] != "0"):
                finger_pos [1] -= 1;
                print ("move L %s:" %( pin_pad[finger_pos[0]][finger_pos[1]] ));
            else:
                print("stayed at current button %s" %( pin_pad[finger_pos[0]][finger_pos[1]] ) );
        print ("calculated key is: %s" %( pin_pad[finger_pos[0]][finger_pos[1]] ));
        passcode += pin_pad[finger_pos[0]][finger_pos[1]];
print ("pascode is: %s" %passcode);
puzzle_in.close();