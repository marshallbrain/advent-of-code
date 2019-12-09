file = open("input.txt", 'r').read()


def get_value(mem, par, modes, output):
    values = []
    modes.reverse()
    for i in range(0, len(modes)):
        if modes[i] == 0:
            if i == output:
                values.append(par[i])
            else:
                try:
                    values.append(mem[par[i]])
                except IndexError:
                    print("error")
                    print(i)
                    print(modes)
                    print(par)
        elif modes[i] == 1:
            values.append(par[i])
        else:
            print("error: unknown mode-", modes[i])
            raise

    return values


def ledding_zero(arr, size):
    while not len(arr) == size:
        arr.insert(0, 0)


def list_to_int(arr):
    num = 0
    arr.reverse()
    for i in range(0, len(arr)):
        num += 10 ** i * arr[i]
    return num


def intcode(mem):
    index = 0
    log = []
    while not mem[index] == 99:
        instruct = [int(x) for x in str(mem[index])]
        modes = instruct[:-2]
        op = list_to_int(instruct[-2:])
        if op == 1:
            ledding_zero(modes, 3)
            a, b, c = get_value(mem, mem[index+1: index+4], modes, 2)
            mem[c] = a + b
            log.append({'index': index, 'input': mem[index: index+4], 'paramaters': [a, b, c], 'output': mem[c]})
            index += 3
        elif op == 2:
            ledding_zero(modes, 3)
            a, b, c = get_value(mem, mem[index+1: index+4], modes, 2)
            mem[c] = a * b
            log.append({'index': index, 'input': mem[index: index+4], 'paramaters': [a, b, c], 'output': mem[c]})
            index += 3
        elif op == 3:
            i = int(input("enter input: "))
            a = mem[index+1]
            mem[a] = i
            log.append({'index': index, 'input': mem[index: index+1], 'paramaters': [a], 'output': mem[a]})
            index += 1
        elif op == 4:
            ledding_zero(modes, 1)
            a = get_value(mem, mem[index+1: index+2], modes, -1)
            a = a[0]
            o = a
            log.append({'index': index, 'input': mem[index: index+2], 'paramaters': [a]})
            if not o == 0:
                for i in log:
                    print(i)
                print(o)
                return
            log.clear()
            print(o)
            index += 1
        elif not op == 99:
            print("error: unknown op-", op)
            raise
        index += 1


def main():
    mem = [int(i) for i in file.split(',')]
    intcode(mem)


main()
