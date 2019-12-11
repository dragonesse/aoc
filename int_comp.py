class IntcodeComp:


    def __init__(self, instr_list):
        self.instr_list = self.initialize_memory(instr_list)
        self.relative_base = 0
        self.instructions = {
            "01" : self.add,
            "02" : self.multiply,
            "07" : self.less_than,
            "08" : self.equals
            }

        self.orders ={
            "05" : self.jump_if_true,
            "06" : self.jump_if_false
        }

    def initialize_memory(self, instr_list):
        return instr_list.copy()

    def parse_modes (self, modes):
        return list(modes)

    def get_value (self, mode, reg_val):
        try:
            if mode == 1:
                return reg_val
            elif mode == 0:
                return int(self.instr_list[reg_val])
            else:
                return int(self.instr_list[reg_val+self.relative_base])
        except IndexError:
            print ("out of memory access, no cell at address %d returning zero" %(reg_val+self.relative_base))
            return 0

    def parse_instr (self,instr):
        instr = str(instr).rjust(5,"0")
        return [self.parse_modes(instr[:-2]) ,instr[-2:]]

    def add (self, val1, val2, position):
        self.insert_result (val1+val2,position)
        return

    def multiply (self, val1, val2, position):
        self.insert_result (val1*val2, position)
        return

    def less_than (self, val1, val2, position):
        self.insert_result (int(val1<val2),position)
        return

    def equals (self, val1, val2, position):
        self.insert_result (int(val1 == val2),position)
        return

    def jump_if_true (self, val1,val2,pointer):
        return val2 if val1 != 0 else pointer

    def jump_if_false (self, val1,val2,pointer):
        return val2 if val1 == 0 else pointer

    def save_input (self, inp, position,mode):
        if mode == 2:
            self.insert_result(inp, position+self.relative_base)
        else:
            self.insert_result(inp, position )
        return

    def insert_result (self, val, position):
        if position < len(self.instr_list):
            self.instr_list [position] = val
        else:
            for i in range(position - len(self.instr_list)):
                self.instr_list += [0]
            self.instr_list += [val]
        return

    # def get_val_at_pos (self, position):
    #     return self.instr_list[position] if position <= len (self.instr_list) else -1

    def calc_pos_for_insert (self, position,mode):

        if mode == 2:
            return position+self.relative_base
        elif mode == 0:
            return position
        else:
            print ("invalid mode for insert operation")
            raise ValueError

    def calc_offset (self, instr):
        if self.is_three_arg_instr(instr):
            return 4
        elif self.is_two_arg_instr (instr):
            return 3
        else:
            return 2

    def is_three_arg_instr (self, instr):
        return instr in self.instructions.keys()

    def is_two_arg_instr (self,instr):
        return instr in self.orders.keys()

    def exec_prog (self, inp):
        pos = 0
        test_inp = inp
        test_out =[]
        while self.instr_list[pos] != "99":
            set_offset = True

            [modes , instr] = self.parse_instr(self.instr_list[pos])

            v1 = self.get_value(int(modes[-1]),int(self.instr_list[pos+1]))
            if self.is_three_arg_instr(instr):
                v2 = self.get_value(int(modes[-2]),int(self.instr_list[pos+2]))
                ins_pos = self.calc_pos_for_insert(int(self.instr_list[pos+3]),int(modes[-3]))
                self.instructions[instr](v1,v2,ins_pos)
            elif self.is_two_arg_instr(instr):
                v2 = self.get_value(int(modes[-2]),int(self.instr_list[pos+2]))
                next_pos = self.orders[instr](v1,v2,pos)
                if next_pos != pos:
                    pos = next_pos
                    set_offset = False
            elif instr == "03":
                v1 = int(self.instr_list[pos+1])
                self.save_input(test_inp,v1,int(modes[-1]))
            elif instr == "09":
                self.relative_base += v1
            else:
                test_out += [v1]

            if set_offset:
                offset = self.calc_offset(instr)
                pos += offset
        return test_out