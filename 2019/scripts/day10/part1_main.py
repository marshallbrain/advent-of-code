file = open("input.txt")


def scan(region, posX, posY):
    width = region.index("\n")
    height = region.count("\n") + 1
    region = list(region)

    x = 0
    y = 0
    for point in region:
        if point == "\n":
            x = 0
            y += 1
            continue

        u = x-posX
        v = y-posY

        if u == 0 and v == 0:
            x += 1
            continue

        i = x
        j = y
        found = False
        while 0 <= i < width and 0 <= j < height:
            if region[j * (width+1) + i] == "#":
                if found:
                    region[j * (width+1) + i] = "."
                else:
                    found = True

            i += u
            j += v

        x += 1

    return region.count("#") - 1


def main():
    region = file.read()

    max = 0
    x = 0
    y = 0
    for point in region:
        if point == "#":
            v = scan(region, x, y)
            if v > max:
                max = v
                print(x, y)

        if point == "\n":
            x = 0
            y += 1
        else:
            x += 1

    print(max)


main()
