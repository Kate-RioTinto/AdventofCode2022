file_obj = open("input.txt", "r")
trees = []

for line in file_obj:
    line = line.strip('\n')
    trees.append(line)
# print(trees)

y_coord = len(trees)

x_coord = len(trees[0])
counter = 0
for x in range(1, x_coord-1):
    for y in range(1, y_coord-1):
        visible_left = True
        visible_right = True
        visible_top = True
        visible_bot = True
        num = int(trees[y][x])
        for k in range(0, y):
            if int(trees[k][x]) >= num:
                visible_left = False
        for l in range(y+1, y_coord):
            if int(trees[l][x]) >= num:
                visible_right = False
        for m in range(0, x):
            if int(trees[y][m]) >= num:
                visible_top = False
        for n in range(x+1, x_coord):
            if(int(trees[y][n])) >= num:
                visible_bot = False
        if visible_left != True and visible_right != True and visible_top != True and visible_bot != True:
            counter = counter
        else:
            counter += 1
# print(counter)
extra = 2*x_coord + 2*(y_coord-2)
counter += extra
print(counter)