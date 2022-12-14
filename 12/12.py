file_obj = open("input.txt", 'r')

lines = []
vals = []

for line in file_obj:
    line = line.strip('\n')
    lines.append(line)

x_coord = len(lines[0])
y_coord = len(lines)

for y in range(y_coord):
    temp = []
    for x in range(x_coord):
        num = ord(lines[y][x]) - ord('a')+1
        if num == -13:
            num = 1
        if num == -27:
            num = 26
        temp.append(num)
    vals.append(temp)


queue = []
moves = [0]
queue.append((0,0))

visited = set()

bfs_traversal = []

while queue:
    current_node = queue.pop(0)
    c_moves = moves.pop(0)
    bfs_traversal.append([current_node, c_moves])
    c_x = current_node[0]
    c_y = current_node[1]

    if (c_x, c_y) not in visited:
        visited.add((c_x, c_y))

        if lines[c_y][c_x]=='E':
            break
        directions = [[c_x+1, c_y], [c_x-1, c_y], [c_x, c_y+1], [c_x, c_y-1]]
        for direction in directions:
            x = direction[0]
            y = direction[1]
            if x in range(x_coord) and y in range(y_coord):
                if vals[c_y][c_x] - vals[y][x] >=-1:
                    queue.append((x,y))
                    moves.append(c_moves+1)

print(bfs_traversal[-1][-1])