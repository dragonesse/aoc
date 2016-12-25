import re;

print("Day 7 puzzle: Internet Protocol Version 7");

tls_cntr = 0;
ssl_cntr   = 0;

pattern = re.compile(r"(.)(.)\2\1");
abba_pattern = re.compile(r"\[[a-z]*(.)(.)\2\1[a-z]*\]");
ssl_pattern_aba = re.compile(r"(.)(.)\1");
ssl_pattern2 = re.compile(r"(.)(.)\1.*\[[a-z]*\2\1\2[a-z]*\]");

#open file
with open('./puzzle_input/day07_test.txt', 'r') as puzzle_in:
    for cur_line in puzzle_in:

        cur_line = cur_line.strip("\n");

        # split hypernet and supernet
        supernet_list = re.split(r"\[.*\]",cur_line);
        hypernet_list = re.split(r"\][a-z]+\[", "]"+cur_line+"[");

        # print (supernet_list);
        # print (hypernet_list);
        # print (cur_line);
        print ("====Processing IP: %s" %cur_line);
        ssl_cntr_cpy = ssl_cntr;

        # a reg pattern aba
        for sn in supernet_list:
            # aba_list = ssl_pattern_aba.findall(sn);
            aba_list = re.findall(r"(?=(.)(.)\1)",sn);
            # if len(aba_list) == 0:
                # print (sn);
            print (aba_list);
            # else:
                # print (sn);
                # print ("aba list empty for supernet: %s" %sn);

            for groups in aba_list:
                # verify it's not aaa
                if groups[0] != groups[1]:
                    # print ("This is aba [%s%s] in supernet: %s" %(groups[0],groups[1],sn));
                    # search for bab in opposite net
                    ssl_pattern_bab = re.compile(r'(?=' + groups[1] + groups[0] + groups[1] + r')');
                    # print(ssl_pattern_bab.pattern);
                    for hn in hypernet_list:
                        if ssl_pattern_bab.search(hn):
                            print ("bab pattern [%s] in hypernet! %s" %(ssl_pattern_bab.pattern,cur_line));
                            # if success, increase counter
                            ssl_cntr += 1;
                            break;
                        # else:
                        #     print ("bab pattern [%s] not found in IP %s" %(ssl_pattern_bab.pattern,cur_line));
        if ssl_cntr == ssl_cntr_cpy:
            print ("SSL not supported in IP: %s" %cur_line);

        abba_list = abba_pattern.findall(cur_line);
        abba_flag  = 0;

        for i in range(len(abba_list)):
            # print (abba_list[i]);
            # exclude patterns of the same letter
            if abba_list[i][0] != abba_list[i][1]:
                # print ("four same chars in IP: %s" %cur_line.strip())
                abba_flag = 1;
                # print ("ABBA in hypernet! Skipping address: %s" %cur_line.strip());
                # print (abba_list);
                break;

        if abba_flag == 0:
            match_list = pattern.findall(cur_line);
            num_expr  = len(match_list);

            for i in range(len(match_list)):
                # print (match_list[i]);
                # exclude patterns of the same letter
                if match_list[i][0] == match_list[i][1]:
                    # print ("four same chars in IP: %s" %cur_line.strip())
                    num_expr -= 1;

            if num_expr > 0:
            # if num_expr == 1:
                # print("IP7 compatible address: %s" %cur_line.strip());
                tls_cntr += 1;

print("number of addresses supporting SSl: %d" %ssl_cntr);
print("number of addresses supporting TLS: %d" %tls_cntr);
puzzle_in.close();