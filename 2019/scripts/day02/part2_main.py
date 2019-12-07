
file = open("input.txt", "r").read()
lines = []
for l in file.split(","):
    lines.append(int(l))


def computer(codes, none, verb):

    codes[1] = none
    codes[2] = verb

    for i in range(0, len(codes), 4):
        o = codes[i]
        if o == 99:
            break
        a = codes[i+1]
        b = codes[i+2]
        c = codes[i+3]
        if o == 1:
            codes[c] = codes[a] + codes[b]
        elif o == 2:
            codes[c] = codes[a] * codes[b]
        else:
            print("error-", i, codes[i], type(i))
            break

    return codes


for a in range(0, 100):
    for b in range(0, 100):
        output = computer(lines.copy(), a, b)
        if output[0] == 19690720:
            print(a, b, 100 * a + b)
