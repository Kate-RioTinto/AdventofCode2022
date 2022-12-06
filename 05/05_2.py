import re

file_obj = open("input.txt", "r")

stacks = []
moves = []
for line in file_obj:
    line = line.strip('\n')
    if line != '':
        if line[0] == 'm':
            moves.append(line.split(' ')[1::2])
        else:
            line = re.sub("\s\s\s\s" , " [_]", line).split()
            stacks.append(line)
num_stacks = int(stacks[-1][-1])
stacks2 = []
for i in range(0, num_stacks):
    stacks2.append([])

del stacks[-1]

for item in stacks:
    i =0
    while i < num_stacks:
        if item[i] != '[_]':
            stacks2[i].append(item[i])
        i += 1

for move in moves:
    num_move = int(move[0])
    from_index = int(move[1])-1
    to_index = int(move[2])-1
    i = 0
    block = []
    while i < num_move:
        block.append(stacks2[from_index].pop(0))
        i += 1
    block.reverse()
    for letter in block:
        stacks2[to_index].insert(0, letter)

final = []
for item in stacks2:
    final.append(item[0].strip('[').strip(']'))        
print(''.join(final))