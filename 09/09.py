import numpy as np
file_obj = open("input.txt", "r")

positions = {'T':[0,0], 'H':[0,0]}
visited = [[0,0]]

for line in file_obj:
    line = line.strip('\n')
    line = line.split(' ')
    moves = int(line[1])
    for i in range(0, moves):
        if line[0] == 'R':
            positions['H'][0] += 1 
        elif line[0] =='L':
            positions['H'][0] -= 1
        elif line[0] == 'U':
            positions['H'][1] += 1
        else:
            positions['H'][1] -= 1

        x_out = positions['H'][0] - positions['T'][0]
        y_out = positions['H'][1] - positions['T'][1]
        
        if abs(x_out) > 1 or abs(y_out) >1:
            positions['T'][0] += np.sign(x_out)
            positions['T'][1] += np.sign(y_out)

        val = []
        val.append(positions['T'][0])
        val.append(positions['T'][1])
        if val not in visited:
            visited.append(val)
print(len(visited))
# print(positions)