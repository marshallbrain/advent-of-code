file = open("input.txt", 'r').readlines()

orbits = {}
for o in file:
    a, b = o.replace('\n', '').split(")")
    orbits[b] = a

total = 0
for b in orbits.values():
    total += 1
    while b in orbits:
        total += 1
        b = orbits[b]

print(total)
