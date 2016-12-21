import hashlib;
import re;
print("Day 5 puzzle: How About a Nice Game of Chess");


door_id     = "uqwqemis";
# door_id     = "abc";

int_index   = 0;
temp = [3231929,5017308,5278568,5357525];
num_found = 0;
# i = 0;

password   = ["","","","","","","",""];

while num_found < 8:
# while i < 4:

    # int_index = temp[i];
    hash_in = door_id+str(int_index);
    hash_vault = hashlib.md5(str.encode(hash_in));

    # print ("current seed %s"  %hash_in);
    # print (hash_vault.hexdigest());

    if re.match('0{5}[0-7]',hash_vault.hexdigest()):
        print (hash_in);
        print (hash_vault.hexdigest());

        if (password[int(hash_vault.hexdigest()[5])] == ""):
            password [int(hash_vault.hexdigest()[5])] = hash_vault.hexdigest()[6];
            print (password);
            num_found += 1;
        else:
            print ("good beginnig, but index already used");
    # i += 1;
    int_index += 1;
print ("password is %s" %password);