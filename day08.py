import re;

print("Day 8 puzzle: Two-Factor Authentication");

#open file
row_max = 6;
col_max = 50;

display    = [[0 for i in range(col_max)] for i in range(row_max)]
pattern_switch = re.compile(r"rect\s+[0-9]+x[0-9]+");
pattern_rot_r  = re.compile(r"rotate\s+row\s+y\=[0-9]+\s+by\s+[0-9]+");
pattern_rot_c   = re.compile(r"rotate\s+column\s+x\=[0-9]+\s+by\s+[0-9]+");

with open('./puzzle_input/day08_test.txt', 'r') as puzzle_in:
    for cur_line in puzzle_in:
        print(cur_line.strip("\n"));

        # split string into array of directions
        directions = cur_line.strip("\n");
        # recognize type of movement
        if (pattern_switch.match(directions)):
            # substract number of pixels to lit
            x_pos   = directions.find("x");
            pix_x   = int(re.sub("rect\s+","",directions[:x_pos]));
            pix_y   = int(directions[x_pos+1:]);
            # turn on rectangular area at the top of the screen
            for i in range (pix_x):
                for j in range (pix_y ):
                    display[i][j] = 1;
            continue;

        if (pattern_rot_r.match(directions)):
            eq_pos   = directions.find("=");
            # max num rows is 6, so we just get char following "="
            row_n = int(directions[eq_pos + 1:eq_pos + 2]);
            shift_n = int(re.sub(".*[0-9]\s+by\s+","",directions[eq_pos + 1:]))
            # print ("row number: %d, shifted by: %d" %(row_n,shift_n));
            for i in range(shift_n):
                cur_row_state = display[row_n][0:];
                # print (cur_row_state);
                for j in range(col_max - 1):
                    display[row_n][j+1] = cur_row_state[j];
                #the first pixel becomes the last one
                display[row_n][0] = cur_row_state[col_max - 1];
            continue;

        if (pattern_rot_c.match(directions)):
            print ("not implemented yet");
            pass;

        for i in range (row_max):
            print (display[i][0:col_max]);

    # count active pixels
    act_cntr = 0;
    for i in range(row_max):
        for j in range (col_max):
            act_cntr += display[i][j];

    print ("number of active pixels: %d" %act_cntr);

puzzle_in.close();