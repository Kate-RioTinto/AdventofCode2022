import ast

file_obj = open("input.txt", 'r')

lines = []
indices = []

for line in file_obj:
    line = line.strip('\n')
    if line != '':
        lines.append(ast.literal_eval(line))
lines2 = []
i = 0
while i < len(lines):
    lines2.append([lines[i], lines[i+1]])
    i += 2

def compare_nums(x, y):
    if type(x) == int and type (y) == int:
        if x > y:
            return False
        elif x < y: 
            return True
    
    if type(y) == int:
        y = [y]
        return compare_nums(x, y)
    if type(x) == int:
        x = [x]    
        return compare_nums(x, y)
    
    if type(x) == list and type (y) == list:    
        i = 0
        while i < len(x) and i < len(y):
            if x[i] != y[i]:
                return compare_nums(x[i],y[i])
            i += 1
        
        if len(x) > len(y):
            return False
        elif len(x) < len(y):
            return True
            
indices = []
length = len(lines2)

for n in range(len(lines2)):
    if compare_nums(lines2[n][0], lines2[n][1]) == True:
        indices.append(n+1)
print(sum(indices))

less_2 = 0
less_6 = 0

for line in lines:
    if compare_nums(line, [[2]]):
        less_2 += 1
    if compare_nums(line, [[6]]):
        less_6 += 1
        
print((less_2+1)*(less_6+2))

# note to self: look up recursion depth stop