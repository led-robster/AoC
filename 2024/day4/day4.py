
part1_occurrences = 0

fh = open("source.txt", 'r')

str_matrix = []
str_len=0

while (line := fh.readline()):
    str_matrix.append(line.strip())

str_len=len(str_matrix[0])
list_len = len(str_matrix)

def find_surroundings(i, j, char, direction):
    # (x,y) + direction
    ret_list = []
    if (i>0 and j>0 and str_matrix[i-1][j-1]==char and (direction=="none" or direction=="NW")):
        ret_list.append([i-1,j-1])
        ret_list.append('NW')
    if (i>0 and str_matrix[i-1][j]==char and (direction=="none" or direction=="N")):
        ret_list.append([i-1,j])
        ret_list.append('N')
    if (i>0 and j<str_len-1 and str_matrix[i-1][j+1]==char and (direction=="none" or direction=="NE")):
        ret_list.append([i-1,j+1])
        ret_list.append('NE')
    if (j>0 and str_matrix[i][j-1]==char and (direction=="none" or direction=="W")):
        ret_list.append([i,j-1])
        ret_list.append('W')
    if (j<str_len-1 and str_matrix[i][j+1]==char and (direction=="none" or direction=="E")):
        ret_list.append([i,j+1])
        ret_list.append('E')
    if (i<list_len-1 and j>0 and str_matrix[i+1][j-1]==char and (direction=="none" or direction=="SW")):
        ret_list.append([i+1,j-1])
        ret_list.append('SW')
    if (i<list_len-1 and str_matrix[i+1][j]==char and (direction=="none" or direction=="S")):
        ret_list.append([i+1,j])
        ret_list.append('S')
    if (i<list_len-1 and j<str_len-1 and str_matrix[i+1][j+1]==char and (direction=="none" or direction=="SE")):
        ret_list.append([i+1,j+1])
        ret_list.append('SE')

    return ret_list
        
# part1 solution
for i in range(0, len(str_matrix)):
    for j in range(0, str_len):
        if (str_matrix[i][j]=='X'):
            level1 = find_surroundings(i,j,'M', "none")
            if (level1):
                for m in range(0,len(level1),2):
                    level2 = find_surroundings(level1[m][0], level1[m][1], 'A', level1[m+1])
                    for n in range(0, len(level2), 2):
                        level3 = find_surroundings(level2[n][0], level2[n][1], 'S', level2[n+1])
                        if (level3):
                            part1_occurrences +=1
                        else:
                            continue
            else:
                continue

        else:
            continue


part2_occurrence = 0
x_cnt = 0

# part2 solution
for i in range(0, len(str_matrix)):
    for j in range(0, str_len):
        if (str_matrix[i][j]=='A'):
            x_cnt = 0
            M_NW = []
            M_NE=[]
            M_SW=[]
            M_SE=[]
            #
            M_NW = find_surroundings(i,j,'M', "NW")
            if (M_NW):
                S_SE = find_surroundings(i,j,'S', "SE")
                if (S_SE):
                    x_cnt += 1
            M_NE = find_surroundings(i,j,'M', "NE")
            if (M_NE):
                S_SW = find_surroundings(i,j,'S',"SW")
                if (S_SW):
                    x_cnt+=1
            M_SW = find_surroundings(i,j,'M', "SW")
            if (M_SW):
                S_NE = find_surroundings(i,j,'S', "NE")
                if (S_NE):
                    x_cnt +=1
            M_SE = find_surroundings(i,j,'M', "SE")
            if (M_SE):
                S_NW = find_surroundings(i,j,'S', "NW")
                if (S_NW):
                    x_cnt +=1

            if (x_cnt==2):
                part2_occurrence+=1


print(part1_occurrences)
print(part2_occurrence)