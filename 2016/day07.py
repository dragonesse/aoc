import re;

print("Day 7 puzzle: Internet Protocol Version 7");

tls_cntr = 0;
ssl_cntr   = 0;

pattern = re.compile(r"(.)(.)\2\1");
abba_pattern = re.compile(r"\[[a-z]*(.)(.)\2\1[a-z]*\]");
ssl_pattern_aba = re.compile(r"(.)(.)\1");

#open file
with open('./puzzle_input/day07.txt', 'r') as puzzle_in:
    for cur_line in puzzle_in:

        cur_line = cur_line.strip("\n");

        # split hypernet and supernet
        supernet_list = re.split(r"\[[a-z]+\]",cur_line);
        hypernet_list = re.split(r"\][a-z]+\[", "]"+cur_line+"[");

        ssl_cntr_cpy = ssl_cntr;

        # a reg pattern aba
        ssl_tag = 0;

        for sn in supernet_list:
            aba_list = re.findall(r"(?=(.)(.)\1)",sn);

            for groups in aba_list:
                # verify it's not aaa
                if groups[0] != groups[1]:
                    # search for bab in opposite net
                    ssl_pattern_bab = re.compile(r'(?=' + groups[1] + groups[0] + groups[1] + r')');

                    for hn in hypernet_list:
                        if ssl_pattern_bab.search(hn):
                            # if success, increase counter
                            ssl_tag = 1;
                            break;
        if ssl_tag == 0:
            print ("SSL not supported in IP: %s" %cur_line);
        else:
            ssl_cntr += 1

        abba_list = abba_pattern.findall(cur_line);
        abba_flag  = 0;

        for i in range(len(abba_list)):
            # exclude patterns of the same letter
            if abba_list[i][0] != abba_list[i][1]:
                abba_flag = 1;
                print ("ABBA in hypernet! Skipping address: %s" %cur_line.strip());
                break;

        if abba_flag == 0:
            match_list = pattern.findall(cur_line);
            num_expr  = len(match_list);

            for i in range(len(match_list)):
                # exclude patterns of the same letter
                if match_list[i][0] == match_list[i][1]:
                    num_expr -= 1;

            if num_expr > 0:
                tls_cntr += 1;

print("number of addresses supporting SSl: %d" %ssl_cntr);
print("number of addresses supporting TLS: %d" %tls_cntr);
puzzle_in.close();