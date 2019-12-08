import math

file = open("input.txt", 'r').read()
# file = "U7,R6,D4,L4\nR8,U5,L5,D3"
# file = "R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83"
# file = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7"


def plot_line(d, s, c, w):
    x = 0
    y = 0
    z = s
    if d == 'R' or d == 'L':
        x = 1
    if d == 'D' or d == 'U':
        y = 1
    if d == 'D' or d == 'L':
        x *= -1
        y *= -1

    while not z == 0:
        c['x'] += x * (z // z)
        c['y'] += y * (z // z)
        c['s'] += 1
        w[(c['x'], c['y'])] = c['s']
        z -= 1


def plot_wire(wire, path):
    cord = {'x': 0, 'y': 0, 's': 0}
    for w in path.split(","):
        plot_line(w[0], int(w[1:]), cord, wire)


def main():
    wire1 = {}
    wire2 = {}

    wires = file.splitlines()
    plot_wire(wire1, wires[0])
    plot_wire(wire2, wires[1])

    cross = wire1.keys() & wire2.keys()
    dist = []
    for x, y in cross:
        d = math.fabs(-x) + math.fabs(-y)
        dist.append(wire1[(x, y)] + wire2[(x, y)])

    print(min(dist))


main()
