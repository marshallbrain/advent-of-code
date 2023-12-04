import re

file = open("input.txt")
file_pattern = "<x=([\\-0-9]+),\\sy=([\\-0-9]+),\\sz=([\\-0-9]+)>"


def abs_sum(list):
    total = 0
    for i in list:
        total += abs(i)
    return total


def main():
    positions = set()
    planets_pos = []
    planets_vel = []

    for line in file.readlines():
        planets_pos.append([int(x) for x in re.findall(file_pattern, line)[0]])
        planets_vel.append([0, 0, 0])

    planets_pos.append([])
    planets_pos.pop()

    steps = 0
    repeat = False
    while not repeat:
        for i in range(len(planets_pos)):
            for j in range(i+1, len(planets_pos)):
                for k in range(3):
                    if planets_pos[i][k] > planets_pos[j][k]:
                        planets_vel[i][k] -= 1
                        planets_vel[j][k] += 1
                    elif planets_pos[i][k] < planets_pos[j][k]:
                        planets_vel[j][k] -= 1
                        planets_vel[i][k] += 1

        for i in range(len(planets_pos)):
            planets_pos[i] = [x + y for x, y in zip(planets_pos[i], planets_vel[i])]

        pos = str(planets_pos + planets_vel)
        if pos in positions:
            repeat = True
        else:
            positions.add(pos)

        steps += 1

    print(steps)


main()
