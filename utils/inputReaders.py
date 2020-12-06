import re

def read_multiline_records_as_list_entries(input_file):
    out_list = []
    empty_line = re.compile(r'^$')
    with open(input_file, 'r') as puzzle_in:
        list_entry = ""
        for cur_line in puzzle_in:
            if re.search(empty_line,cur_line.strip()) is None:
                list_entry += ' ' + cur_line.strip()
            else:
                # need to get rid of 1st space
                out_list.append(list_entry[1:].split(" "))
                list_entry = ""
        # need to flush the last entry, in case it's not followed by new line
        out_list.append(list_entry[1:].split(" "))
    puzzle_in.close()
    return out_list

def read_oneline_records_as_list_entries(input_file):
    out_list = []
    with open(input_file, 'r') as puzzle_in:
        out_list = [cur_line.strip() for cur_line in puzzle_in]
    puzzle_in.close()
    return out_list

def read_int_records_as_list_entries(input_file):
    out_list = []
    with open(input_file, 'r') as puzzle_in:
        out_list = [int(cur_line) for cur_line in puzzle_in]
    puzzle_in.close()
    return out_list

def read_map(input_file):
    out_map = []
    with open(input_file, 'r') as puzzle_in:
        for cur_line in puzzle_in:
            out_map.append(cur_line.strip().replace(".","0").replace("#","1"))
    puzzle_in.close()
    return out_map
