file_obj = open("input.txt", "r")

chars = ''
for line in file_obj:
    line = line.strip('\n')
    chars = line
i = 0
print(chars)
while i < len(chars)-4:
    block = chars[i:i+4]
    signal = True
    for char in block:
        if block.count(char) >= 2:
            signal = False
    if signal == True:
        print(block, i+4)
        break
    else:
        i = i + 1
    print(block)