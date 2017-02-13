import re;

print("Day 8 puzzle: Two-Factor Authentication");

#open file
row_max = 6;
col_max = 50;

display    = [[0 for i in range(col_max)] for i in range(row_max)]
pattern_switch = re.compile(r"rect\s+[0-9]+x[0-9]+");
pattern_rot_r  = re.compile(r"rotate\s+row\s+y\=[0-9]+\s+by\s+[0-9]+");
pattern_rot_c   = re.compile(r"rotate\s+column\s+x\=[0-9]+\s+by\s+[0-9]+");

with open('./puzzle_input/day08.txt', 'r') as puzzle_in:
    for cur_line in puzzle_in:
        print(cur_line.strip("\n"));

        # split string into array of directions
        directions = cur_line.strip("\n");
        # recognize type of movement
        if (pattern_switch.match(directions)):
            # substract number of pixels to lit
            x_pos   = directions.find("x");
            # get number before "x" char
            pix_y   = int(re.sub("rect\s+","",directions[:x_pos]));
            #max number of rows is 6
            pix_x   = int(directions[x_pos+1:]);
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

            for i in range(shift_n):
                cur_row_state = display[row_n][0:];
                # print (cur_row_state);
                for j in range(col_max - 1):
                    display[row_n][j+1] = cur_row_state[j];
                #the first pixel becomes the last one
                display[row_n][0] = cur_row_state[col_max - 1];
            continue;

        if (pattern_rot_c.match(directions)):
            eq_pos   = directions.find("=");
            # get column number
            #rotate column x=30 by 1
            col_n = int(re.sub(r'([0-9]+)\s+.*',r'\1',directions[eq_pos + 1:]));
            shift_n = int(re.sub(".*[0-9]+\s+by\s+","",directions[eq_pos + 1:]))
            cur_col_state = [0 for i in range (row_max)];
            for i in range(shift_n):
                for x in range (row_max):
                    cur_col_state [x] = display[x][col_n];
                for j in range(row_max - 1):
                    display[j+1][col_n] = cur_col_state[j];
                #the first pixel becomes the last one
                display[0][col_n] = cur_col_state[row_max - 1];
            continue;

    # count active pixels
    act_cntr = 0;
    for i in range(row_max):
        for j in range (col_max):
            act_cntr += display[i][j];

    print ("number of active pixels: %d" %act_cntr);


    for i in range (row_max):
        for j in range (col_max):
            if (display [i][j] == 1):
                display[i][j] = "*";
            else:
                display[i][j] = " ";

    for j in range (10):
        print ("letter %d:" %j);
        for i in range (row_max):
            print (display[i][j*5:(j+1)*5]);

puzzle_in.close();