file = open("input.txt", 'r').read()
file = [char for char in file]

image = []
layer = ""
z = 0
while len(file) > 0:
    image.append([])
    c_layer = ""
    for y in range(0, 6):
        image[z].append([])
        for x in range(0, 25):
            i = file.pop(0)
            c_layer += i
            image[z][y].append(i)
    if len(layer) == 0 or c_layer.count('0') < layer.count('0'):
        layer = c_layer
    z += 1

print(layer.count('1') * layer.count('2'))
