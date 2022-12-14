import math
file_obj = open("input.txt", 'r')

lines = []

monkeys = []
for line in file_obj:
    line = line.strip('\n').split()
    if line != '':
        lines.append(line)
count = 1
things = []
ops = []
inspections = []
item_list = dict()
i = 0
counter = 0
worry_down = 1
while i < len(lines):
    if lines[i] != []:
        if lines[i][0] == 'Monkey':
            things = []
            items = lines[i+1][2:]
            for item in items:
                things.append(int(item.strip(',')))
            ops = lines[i+2][-2:]
            divis = int(lines[i+3][-1])
            true_throw = int(lines[i+4][-1])
            false_throw = int(lines[i+5][-1])
            worry_down = worry_down*divis
            monkeys.append([ops, divis, true_throw, false_throw])
            i = i + 5
            inspections.append(0)
            item_list[counter] = things
            counter += 1
    i += 1
    # print(monkeys)
for x in range(10000):
    i = 0
    while i < len(monkeys):
        monkey = monkeys[i]
        if item_list[i] != None:
            range_val = len(item_list[i])
            for n in range(0, range_val):
                num = item_list[i].pop(0)
                inspections[i] += 1
                if monkey[0][0] == '*':
                    if monkey[0][1]!='old':
                        num = num * int(monkey[0][1])
                    else:
                        num = num * num
                elif monkey[0][0] == '+':
                    if monkey[0][1]!='old':
                        num = num + int(monkey[0][1])
                    else:
                        num = num + num
                elif monkey[0][0] == '-':
                    if monkey[0][1]!='old':
                        num = num - int(monkey[0][1])
                    else:
                        num = num - num
                elif monkey[0][0] == '/':
                    if monkey[0][1]!='old':
                        num = num / int(monkey[0][1])
                    else:
                        num = num / num
                # num = num // 3
                divis = monkey[1]
                
                if num%divis == 0:
                    monkey_to = monkey[2]
                else:
                    monkey_to = monkey[3]
                num = num % worry_down
                if item_list[monkey_to] != None:
                    item_list[monkey_to].append(num)
                else:
                    item_list[monkey_to] = []
                    item_list[monkey_to].append(num)
        i += 1
inspections.sort(reverse=True)
print(inspections[0]*inspections[1])