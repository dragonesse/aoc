import math;

print("Day 1 puzzle: No time for Taxicab");

#open file
start_x, end_x, start_y, end_y = 0, 0, 0, 0 ;

with open('./puzzle_input/day01_test.txt', 'r') as puzzle_in:
    for cur_line in puzzle_in:
        turn_cntr = 0;
        print(cur_line.strip("\n"));

        # split string into array of directions
        directions = cur_line.split(",");

        # calculate actual move
        look_at     = "N";
        for hint in directions:
            hint = hint.strip();
            turn_dir, dist = hint[0], hint[1:];
            # y axis
            if (turn_cntr % 2):
                if (turn_dir == "L" ) and (look_at == "E"):
                    end_y += int(dist);
                    look_at = "N";
                elif (turn_dir == "R" ) and (look_at == "E") :
                    end_y -= int(dist);
                    look_at = "S";
                elif (turn_dir == "L") and (look_at == "W"):
                    end_y -= int(dist);
                    look_at = "S";
                elif (turn_dir == "R") and (look_at == "W"):
                    end_y += int(dist);
                    look_at = "N";
            # x axis
            else:
                if (turn_dir == "R") and (look_at == "N"):
                     end_x += int(dist);
                     look_at = "E";
                elif (turn_dir == "L") and (look_at == "N"):
                     end_x -= int(dist);
                     look_at = "W";
                elif (turn_dir == "R") and (look_at == "S"):
                    end_x -= int(dist);
                    look_at = "W";
                elif (turn_dir == "L") and (look_at == "S"):
                    end_x += int(dist);
                    look_at ="E"

            turn_cntr += 1;
            print("%s end x, end y: %d %d" %(hint, end_x, end_y) );
        distance = math.fabs(start_x-end_x) + math.fabs(start_y-end_y);
        start_x, end_x, start_y, end_y = 0, 0, 0, 0 ;
        print("distance is %d" %distance);
puzzle_in.close();