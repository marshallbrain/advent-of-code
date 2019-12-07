file = open("day-01_input.txt", "r")


def get_fuel(mass):
    fuel = mass // 3 - 2
    if fuel <= 0:
        return 0
    return fuel + get_fuel(fuel)


total = 0
for i in file.read().split("\n"):
    m = int(i)
    total = total + get_fuel(m)

print(total)


