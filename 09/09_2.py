import numpy as np
file_obj = open("input.txt", "r")

positions = []
for i in range (0,10):
    positions.append([0,0])

visited = [[0,0]]

for line in file_obj:
    line = line.strip('\n')
    line = line.split(' ')
    moves = int(line[1])
    for i in range(0, moves):
        if line[0] == 'R':
            positions[0][0] += 1 
        elif line[0] =='L':
            positions[0][0] -= 1
        elif line[0] == 'U':
            positions[0][1] += 1
        else:
            positions[0][1] -= 1
        for i in range(0,9):
            x_out = positions[i][0] - positions[i+1][0]
            y_out = positions[i][1] - positions[i+1][1]
        
            if abs(x_out) > 1 or abs(y_out) >1:
                positions[i+1][0] += np.sign(x_out)
                positions[i+1][1] += np.sign(y_out)

        val = []
        val.append(positions[9][0])
        val.append(positions[9][1])
        if val not in visited:
            visited.append(val)
print(len(visited))
# print(positions)