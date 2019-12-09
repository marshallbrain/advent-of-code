file = open("input.txt", 'r').readlines()


def min_score(keys, scores):
    items = list(scores.items())
    min_item = (['', 9999])
    for i in keys:
        if scores[i] < min_item[1]:
            min_item = (i, scores[i])
    return min_item


def a_star(s, g, orbit_map):
    # // The set of discovered nodes that may need to be (re-)expanded.
    # // Initially, only the start node is known.
    dist = set()  # openSet
    dist.add(s)

    # // For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from start to n currently
    # known.
    path = {}  # cameFrom

    # // For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
    g_score = {s: 0}

    # // For node n, fScore[n] := gScore[n] + h(n).
    f_score = {s: 1}

    while not len(dist) == 0:
        current = min_score(dist, f_score)[0]  # the node in openSet having the lowest fScore[] value
        if current == g:
            return g_score[current]

        dist.remove(current)
        array = []
        if orbit_map[current][2]:
            array += orbit_map[current][2]
        if not orbit_map[current][1] == '':
            array += [orbit_map[current][1]]
        for n in array:
            # // d(current,neighbor) is the weight of the edge from current to neighbor
            # // tentative_gScore is the distance from start to the neighbor through current
            tentative_g_score = g_score[current] + 1
            if tentative_g_score < g_score.get(n, 9999):
                # // This path to neighbor is better than any previous one. Record it!
                path[n] = current
                g_score[n] = tentative_g_score
                f_score[n] = g_score[n] + 1
                if n not in dist:
                    dist.add(n)


orbits = {}
for o in file:
    a, b = o.replace('\n', '').split(")")
    if a not in orbits:
        orbits[a] = [a, '', []]
    if b not in orbits:
        orbits[b] = [b, '', []]
    orbits[a][2].append(b)
    orbits[b][1] = a

start = 'YOU'
end = 'SAN'

d = a_star(start, end, orbits)-2
print(d)
