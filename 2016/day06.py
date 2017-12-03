print("Day 6 puzzle: Signals and Noise");


message = "";

set1    = {};
set2    = {};
set3    = {};
set4    = {};
set5    = {};
set6    = {};
set7    = {};
set8    = {};

num_lines = 0;
#open file
with open('./puzzle_input/day06.txt', 'r') as puzzle_in:

    for cur_line in puzzle_in:
        print(cur_line.strip("\n"));

        # split string into array of directions
        input_data = cur_line.strip("\n");

        #make hashes letter:num of repetition
        if input_data[0] in set1:
            set1[input_data[0]] -= 1;
        else:
            set1[input_data[0]] = 0;

        if input_data[1] in set2:
            set2[input_data[1]] -= 1;
        else:
            set2[input_data[1]] = 0;

        if input_data[2] in set3:
            set3[input_data[2]] -= 1;
        else:
            set3[input_data[2]] = 0;

        if input_data[3] in set4:
            set4[input_data[3]] -= 1;
        else:
            set4[input_data[3]] = 0;

        if input_data[4] in set5:
            set5[input_data[4]] -= 1;
        else:
            set5[input_data[4]] = 0;

        if input_data[5] in set6:
            set6[input_data[5]] -= 1;
        else:
            set6[input_data[5]] = 0;

        if input_data[6] in set7:
            set7[input_data[6]] -= 1;
        else:
            set7[input_data[6]] = 0;

        if input_data[7] in set8:
            set8[input_data[7]] -= 1;
        else:
            set8[input_data[7]] = 0;
        num_lines += 1;

    max_num = -1*num_lines;
    letter = "";
    for key_letter in set1:
        if set1[key_letter] > max_num:
            max_num = set1[key_letter];
            letter = key_letter;
    message += letter;

    max_num = -1*num_lines;
    letter = "";
    for key_letter in set2:
        if set2[key_letter] > max_num:
            max_num = set2[key_letter];
            letter = key_letter;
    message += letter;

    max_num = -1*num_lines;
    letter = "";

    for key_letter in set3:
        if set3[key_letter] > max_num:
            max_num = set3[key_letter];
            letter = key_letter;
    message += letter;

    max_num = -1*num_lines;
    letter = "";

    for key_letter in set4:
        if set4[key_letter] > max_num:
            max_num = set4[key_letter];
            letter = key_letter;
    message += letter;

    max_num = -1*num_lines;
    letter = "";

    for key_letter in set5:
        if set5[key_letter] > max_num:
            max_num = set5[key_letter];
            letter = key_letter;
    message += letter;

    max_num = -1*num_lines;
    letter = "";

    for key_letter in set6:
        if set6[key_letter] > max_num:
            max_num = set6[key_letter];
            letter = key_letter;
    message += letter;

    max_num = -1*num_lines;
    letter = "";

    for key_letter in set7:
        if set7[key_letter] > max_num:
            max_num = set7[key_letter];
            letter = key_letter;
    message += letter;

    max_num = -1*num_lines;
    letter = "";

    for key_letter in set8:
        if set8[key_letter] > max_num:
            max_num = set8[key_letter];
            letter = key_letter;
    message += letter;

print ("the message is %s" %message);
puzzle_in.close();