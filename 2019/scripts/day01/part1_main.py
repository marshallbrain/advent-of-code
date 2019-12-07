file = open("day-01_input.txt", "r")

total = 0
for i in file.read().split("\n"):
    m = int(i)
    f = m // 3 - 2
    total = total + f

print(total)
