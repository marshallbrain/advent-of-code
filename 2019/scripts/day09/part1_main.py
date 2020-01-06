log = []


def append_zeros(num_list, size):
    new_list = []
    num_list.reverse()
    for i in range(0, size):
        if i < len(num_list):
            new_list.append(int(num_list[i]))
        else:
            new_list.append(0)
    return new_list


def compute(mem, index, relative_base, input_num, output_num, fun, debug):
    code = [char for char in str(mem[index])]
    modes = append_zeros(code[:-2], input_num + output_num)
    input_loc = mem[index + 1: index + 1 + input_num]
    output_loc = mem[index + 1 + input_num: index + 1 + input_num + output_num]

    inputs = input_loc.copy()
    for i in range(0, input_num):
        mode = modes[i]
        if mode == 0:
            inputs[i] = mem[inputs[i]]
        elif mode == 1:
            pass
        elif mode == 2:
            inputs[i] = mem[inputs[i]+relative_base]
        else:
            print("error, mode-", mode)
            raise
    outputs = [fun(*inputs)]
    for i in range(0, output_num):
        mode = modes[i + input_num]
        if mode == 0:
            mem[output_loc[i]] = outputs[i]
        elif mode == 2:
            mem[output_loc[i]+relative_base] = outputs[i]
        else:
            print("error, mode-", mode)
            raise
    if debug:
        log.append(
            {'index': index, 'input': [mem[index]] + input_loc + output_loc, 'paramaters': inputs, 'output': outputs})
    return 1 + input_num + output_num


def append_ints(num_list):
    num = 0
    for i in range(1, len(num_list) + 1):
        num += 10 ** (len(num_list) - i) * int(num_list[i - 1])
    return num


def intcode(mem, index=0, relative_base=0, input_list=(), debug=False, stop_after_print=False):
    input_list = list(input_list)
    output_list = []
    op = 0
    while not op == 99:
        op = append_ints(str(mem[index])[-2:])
        if op == 1:
            index += compute(mem, index, relative_base, 2, 1, lambda a, b: a + b, debug)
        elif op == 2:
            index += compute(mem, index, relative_base, 2, 1, lambda a, b: a * b, debug)
        elif op == 3:
            if input_list:
                input_override = input_list.pop(0)
            else:
                input_override = int(input("enter input: "))
            index += compute(mem, index, relative_base, 0, 1, lambda: input_override, debug)
        elif op == 4:
            index += compute(mem, index, relative_base, 1, 0, lambda a: output_list.append(a), debug)
            if debug:
                for i in log:
                    print(i)
                log.clear()
                print(output_list[-1])
                print()
            if stop_after_print:
                return output_list[-1], mem, index
            else:
                print(output_list[-1])
        elif op == 5:
            new_index = []

            def not_zero(a, b):
                if a != 0:
                    x = new_index
                    x.append(b)

            index += compute(mem, index, relative_base, 2, 0, not_zero, debug)
            if new_index:
                index = new_index[0]
        elif op == 6:
            new_index = []

            def is_zero(a, b):
                if a == 0:
                    x = new_index
                    x.append(b)

            index += compute(mem, index, relative_base, 2, 0, is_zero, debug)
            if new_index:
                index = new_index[0]
        elif op == 7:
            index += compute(mem, index, relative_base, 2, 1, lambda a, b: 1 if a < b else 0, debug)
        elif op == 8:
            index += compute(mem, index, relative_base, 2, 1, lambda a, b: 1 if a == b else 0, debug)
        elif op == 9:
            r_base = [relative_base]

            def offset_base(a):
                x = r_base
                x[0] += a
            index += compute(mem, index, relative_base, 1, 0, offset_base, debug)
            relative_base = r_base[0]
        elif op != 99:
            print('error, op code-', op)
            for i in log:
                print(i)
            raise
    return output_list, [], 0


file = open("input.txt", 'r').read()


def main():
    mem = [int(i) for i in file.split(',')]
    while len(mem) < 2000:
        mem.append(0)
    intcode(mem)


main()
