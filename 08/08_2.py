file_obj = open("input.txt", "r")
trees = []

for line in file_obj:
    line = line.strip('\n')
    trees.append(line)
# print(trees)

y_coord = len(trees)

x_coord = len(trees[0])

sight_vals = []
for x in range(1, x_coord-1):
    for y in range(1, y_coord-1):
        left_count = 0
        right_count = 0
        top_count = 0
        bot_count = 0
        num = int(trees[y][x])
        k = y-1
        
        while k >= 0:
            if int(trees[k][x]) >= num:
                left_count += 1
                break
            else:
                left_count += 1
            k = k - 1
        l = y+1
        
        while l < y_coord:
            if int(trees[l][x]) >= num:
                right_count += 1
                break
            else:
                right_count += 1
            l += 1
            
        m = x-1
        while m>=0:
            if int(trees[y][m]) >= num:
                top_count += 1
                break
            else:
                top_count += 1
            m = m-1
            
        n = x+1
        while n < x_coord:
            if(int(trees[y][n])) >= num:
                bot_count +=1
                break
            else:
                bot_count += 1
            n += 1
            
        sight_vals.append(bot_count*top_count*right_count*left_count)

print(max(sight_vals))