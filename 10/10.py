file_obj = open("input.txt", 'r')

X = 1
total = 0
counter = 0
nums = []
outputs = []
output = ''

for line in file_obj:
    line = line.strip('\n').split()
    nums.append(0)
    if line[0]=="addx":
        nums.append(int(line[1]))

for num in nums:
    counter +=1
    if len(output) <= X+1 and len(output) >= X-1:
            output += '#'
    else:
        output += '.'
    if len(output) == 40:
        outputs.append(output)
        output = ''
    if (counter-20)%40 == 0:
        total += X*counter
    X += num

print(total)
for output in outputs:
    print(output)