import math

file = open("input.txt")

cord_x = 17
cord_y = 22


def sort_ang(e):
    return e[0]


def main():
    region = file.read()
    angles_pos = []
    angles_neg = []

    i = 0
    j = 0
    for point in region:
        x = i-cord_x
        y = j-cord_y

        if x == 0 and y == 0:
            i += 1
            continue

        if point == "#":

            if x == 0:
                if y > 0:
                    ang = math.inf
                else:
                    ang = -math.inf
            else:
                ang = y/x
            if x < 0:
                angles_neg.append([ang, x, y])
            else:
                angles_pos.append([ang, x, y])

        if point == "\n":
            i = 0
            j += 1
        else:
            i += 1

    angles_pos.sort(key=sort_ang)
    angles_neg.sort(key=sort_ang)

    angles = angles_pos + angles_neg

    i = 0
    ang = ""
    count = 0
    while len(angles) > 0:
        if i >= len(angles):
            i = 0

        angle = angles[i]

        if i < len(angles)-1:
            angle_next = angles[i+1]
            if angle[0] == angle_next[0]:
                if abs(angle[1]) > abs(angle_next[1]) or abs(angle[2]) > abs(angle_next[2]):
                    i += 1
                    continue

            if ang != "" and angle[0] == ang:
                i += 1
                continue

        count += 1
        print(count, angle[1]+cord_x, angle[2]+cord_y)
        ang = angles.pop(i)[0]


main()