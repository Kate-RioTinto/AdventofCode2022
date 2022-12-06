file_obj = open("input.txt", "r")

lines = []
total = 0

for line in file_obj:
    line = line.strip('\n')
    lines.append(line)
i=0
while i <= len(lines)-3:
    line1 = lines[i]
    line2 = lines[i+1]
    line3 = lines[i+2]
    
    match1 = set(line1).intersection(line2)
    print(match1)
    match2 = set(match1).intersection(line3)
    print(match2)
    for m in match2:
        if m[0].islower():
            total += ord(m)-96
        else:
            total += ord(m)-38
    i = i + 3
print(total)
