from scripts.day13.part1_intcode import IntCode

file = open("input.txt")


def main():
    intcode = IntCode(file.read(), 3000)
    output = intcode.get_output([], False)

    count = 0
    for i in range(2, len(output), 3):
        if output[i] == 2:
            count += 1

    print(count)


main()
