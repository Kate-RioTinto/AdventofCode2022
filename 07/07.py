i = 1
key_vals = []
sum_val = 0
size_dict = {}

file_obj = open("input.txt", "r")
for line in file_obj:
    line = line.split()
    if len(line) >=3 and line[2] == "..":
        key_vals.pop()
        sum_val = 0
    elif line[0] == "$" and line[1] == "cd":
        key_vals.append(i)
        size_dict[i] = 0
        i += 1
    elif line[0].isdigit():
        num = int(line[0])
        for key in key_vals:
            size_dict[key] += num
total = 0
deletables = []
target_val = 30000000 - (70000000 - size_dict[1])

for item in size_dict.values():
    if item <= 100000:
        total += item
    if item >= target_val:
        deletables.append(item)
        
print(total, min(deletables))