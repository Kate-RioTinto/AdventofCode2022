calories = []
sum_cal = 0

file_obj = open("input.txt", "r")
for line in file_obj:
    if line != '\n':
        sum_cal += int(line)
    else:
        calories.append(sum_cal)
        sum_cal = 0
file_obj.close()

calories.sort(reverse = True)

print(calories[0])
print(sum(calories[0:3]))