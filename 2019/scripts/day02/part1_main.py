codes = []
file = open("input.txt", "r").read()

# file = "2,4,4,5,99,0"
for i in file.split(","):
    codes.append(int(i))

codes[1] = 12
codes[2] = 2

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

print(codes)
