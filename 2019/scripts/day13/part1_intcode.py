class IntCode:
    def __init__(self, program, mem_size):
        self.mem = [int(i) for i in program.split(',')]
        while len(self.mem) < mem_size:
            self.mem.append(0)

        self.pointer = 0
        self.op = [0]
        self.input = []
        self.output = []
        self.base = 0

    def get_position(self, index):
        if self.op[index] == 0:
            return self.mem[self.pointer+index]
        if self.op[index] == 2:
            return self.base + self.mem[self.pointer+index]

    def get_args(self, count):
        args = []
        for i in range(count):
            mode = self.op[i+1]

            if mode == 1:
                args.append(self.mem[self.pointer+i+1])
            else:
                args.append(self.mem[self.get_position(i+1)])
        return args

    def operations(self):
        op = self.op[0]
        if op == 1:
            args = self.get_args(2)
            output = self.get_position(3)

            self.mem[output] = args[0] + args[1]
            self.pointer += 4
        elif op == 2:
            args = self.get_args(2)
            output = self.get_position(3)

            self.mem[output] = args[0] * args[1]
            self.pointer += 4
        elif op == 3:
            if len(self.input) <= 0:
                raise ValueError
            self.mem[self.get_position(1)] = self.input.pop()
            self.pointer += 2
        elif op == 4:
            self.output.append(self.get_args(1)[0])
            self.pointer += 2
        elif op == 5:
            args = self.get_args(2)
            if args[0] != 0:
                self.pointer = args[1]
            else:
                self.pointer += 3
        elif op == 6:
            args = self.get_args(2)
            if args[0] == 0:
                self.pointer = args[1]
            else:
                self.pointer += 3
        elif op == 7:
            args = self.get_args(2)
            output = self.get_position(3)
            if args[0] < args[1]:
                self.mem[output] = 1
            else:
                self.mem[output] = 0
            self.pointer += 4
        elif op == 8:
            args = self.get_args(2)
            output = self.get_position(3)
            if args[0] == args[1]:
                self.mem[output] = 1
            else:
                self.mem[output] = 0
            self.pointer += 4
        elif op == 9:
            args = self.get_args(1)
            self.base += args[0]
            self.pointer += 2
        else:
            raise RuntimeError

    def set_op(self):
        op = str(self.mem[self.pointer])[::-1]
        self.op = [int(op[:2][::-1])] + [int(i) for i in op[2:]]
        while len(self.op) < 4:
            self.op.append(0)

    def cycle(self):
        self.set_op()
        while self.op[0] != 99:
            self.operations()
            self.set_op()
        self.output.append(99)

    def get_output(self, args, clear=False):
        self.input = [args] if isinstance(args, int) else args.reverse()

        try:
            self.cycle()
        except ValueError:
            pass

        if clear:
            output = self.output
            self.output = []
            return output

        return self.output
