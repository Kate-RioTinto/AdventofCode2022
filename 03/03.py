# print(ord('a')-96)
# print(ord('z')-96)
# print(ord('A')-38)
# print(ord('B')-38)
same = 0
file_obj = open("input.txt", "r")

for line in file_obj:
    match = ''
    line = line.strip('\n')
    firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
    print(firstpart, secondpart)
    for char in firstpart:
        for char2 in secondpart:
            if ord(char) == ord(char2):
                match = char
    if match != '':
        if match.islower():
            same += ord(match)-96
        else:
            same += ord(match)-38 
print(same)