from scripts.day11.part1_intcode import IntCode

file = open("input.txt")

move = (
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
)


def main():
    hull = {(0, 0): 1}
    intcode = IntCode(file.read(), 2000)

    output = []
    pos = (0, 0)
    head = 0
    while len(output) < 3:
        color = hull.get(pos, 0)
        output = intcode.get_output(color, True)
        hull[pos] = output[0]

        if output[1] == 0:
            head -= 1
        elif output[1] == 1:
            head += 1

        m = move[head % 4]
        pos = (pos[0] + m[0], pos[1] + m[1])

    minx = 0
    miny = 0
    maxx = 0
    maxy = 0
    for key in hull.keys():
        minx = min(minx, key[0])
        miny = min(miny, key[1])
        maxx = max(maxx, key[0])
        maxy = max(maxy, key[1])

    code = []
    for _ in range(miny, maxy+1):
        code.append(["0"]*(maxx - minx + 1))
    for [pos, color] in hull.items():
        code[pos[1] - miny][pos[0]] = str(color)

    for line in code:
        print(
            "".join(line)
            .replace("0", " ")
            .replace("1", "#")
        )


main()
