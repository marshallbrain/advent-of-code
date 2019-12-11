file = open("input.txt", 'r').read()
file = [char for char in file]

image_layers = []
z = 0
while len(file) > 0:
    image_layers.append([])
    for y in range(0, 6):
        image_layers[z].append([])
        for x in range(0, 25):
            image_layers[z][y].append(file.pop(0))
    z += 1

image = []
for z in range(0, len(image_layers)):
    for y in range(0, len(image_layers[z])):
        image.append([])
        for x in range(0, len(image_layers[z][y])):
            if len(image[y]) <= x:
                image[y].append(image_layers[z][y][x])
            else:
                if image[y][x] == '2':
                    image[y][x] = image_layers[z][y][x]
        if len(image[-1]) == 0:
            image.pop(-1)

for y in image:
    for x in y:
        print(x, end='')
    print()
