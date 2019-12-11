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


def compute(mem, index, input_num, output_num, fun, debug):
    code = [char for char in str(mem[index])]
    modes = append_zeros(code[:-2], input_num + output_num)
    input_loc = mem[index + 1: index + 1 + input_num]
    output_loc = mem[index + 1 + input_num: index + 1 + input_num + output_num]

    inputs = input_loc.copy()
    for i in range(0, input_num):
        mode = modes[i]
        val = inputs[i]
        if mode == 0:
            inputs[i] = mem[val]
        elif mode == 1:
            pass
        else:
            print("error, mode-", mode)
            raise
    outputs = [fun(*inputs)]
    for i in range(0, output_num):
        mode = modes[i + input_num]
        if mode == 0:
            mem[output_loc[i]] = outputs[i]
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


def intcode(mem, input_list=(), debug=False):
    input_list = list(input_list)
    output_list = []
    index = 0
    op = 0
    while not op == 99:
        op = append_ints(str(mem[index])[-2:])
        if op == 1:
            index += compute(mem, index, 2, 1, lambda a, b: a + b, debug)
        elif op == 2:
            index += compute(mem, index, 2, 1, lambda a, b: a * b, debug)
        elif op == 3:
            if input_list:
                input_override = input_list.pop(0)
            else:
                input_override = int(input("enter input: "))
            index += compute(mem, index, 0, 1, lambda: input_override, debug)
        elif op == 4:
            index += compute(mem, index, 1, 0, lambda a: output_list.append(a), debug)
            if debug:
                for i in log:
                    print(i)
                log.clear()
                print(output_list[-1])
                print()

        elif op == 5:
            new_index = []

            def not_zero(a, b):
                if a != 0:
                    x = new_index
                    x.append(b)

            index += compute(mem, index, 2, 0, not_zero, debug)
            if new_index:
                index = new_index[0]
        elif op == 6:
            new_index = []

            def is_zero(a, b):
                if a == 0:
                    x = new_index
                    x.append(b)

            index += compute(mem, index, 2, 0, is_zero, debug)
            if new_index:
                index = new_index[0]
        elif op == 7:
            index += compute(mem, index, 2, 1, lambda a, b: 1 if a < b else 0, debug)
        elif op == 8:
            index += compute(mem, index, 2, 1, lambda a, b: 1 if a == b else 0, debug)
        elif op != 99:
            print('error, op code-', op)
            for i in log:
                print(i)
            raise
    return output_list


file = open("input.txt", 'r').read()


def main(amp_code):
    mem_input = [int(i) for i in file.split(',')]

    output = [0]
    for sig in amp_code:
        output = output + (intcode(mem_input, debug=False, input_list=[sig, output[-1]]))
    return output


amp = range(0, 5)
max_sig = [0]
for a1 in amp:
    amp1 = [a1]
    for a2 in [x for x in amp if x not in amp1]:
        amp2 = amp1 + [a2]
        for a3 in [x for x in amp if x not in amp2]:
            amp3 = amp2 + [a3]
            for a4 in [x for x in amp if x not in amp3]:
                amp4 = amp3 + [a4]
                for a5 in [x for x in amp if x not in amp4]:
                    signal = main(amp4 + [a5])
                    if signal[-1] > max_sig[-1]:
                        max_sig = signal

print(max_sig)
