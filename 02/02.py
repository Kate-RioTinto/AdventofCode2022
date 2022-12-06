# A or X = rock (1)
# B or Y = paper (2)
# C or Z = scissors (3)

# win = 6, lose = 0, draw = 3

# second part: X lose, Y draw, Z win

total_score = 0
total_score2 = 0

dict_first = { 'A X' : 4, 'A Y' : 8, 'A Z' : 3, 'B X' : 1, 'B Y' : 5, 'B Z' : 9, 'C X' : 7, 'C Y' : 2, 'C Z' : 6 }
dict_sec = {'A X' : 3, 'A Y' : 4, 'A Z' : 8, 'B X' : 1, 'B Y' : 5, 'B Z' : 9, 'C X' : 2, 'C Y' : 6, 'C Z' : 7 }

file_obj = open("input.txt", "r")

for line in file_obj:
    line = line.strip('\n')
    total_score += dict_first[line]
    total_score2 += dict_sec[line]
    
print(total_score, total_score2)