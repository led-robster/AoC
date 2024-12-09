

fh = open("source.txt", 'r')

map = []


while (line := fh.readline()):
    map.append(list(line.strip()))

width = len(map[0])
height = len(map)


guard_out = False
up = True
right = False
left = False
down = False
traversed_path = []

# next movement can : 1. bring the guard outside 2. simple move the guard 3. guard meets an obstacle

while (not guard_out):

    up = False
    right = False
    left = False
    down = False
    
    for i in range(0, height):
        for j in range(0, width):
            if (map[i][j]=='^'):
                guard_x = i
                guard_y = j
                new_guard='^'
                up=True
            elif (map[i][j]=='>'):
                guard_x = i
                guard_y = j
                new_guard='>'
                right=True
            elif (map[i][j]=='<'):
                guard_x = i
                guard_y = j
                new_guard='<'
                left=True
            elif (map[i][j]=='v'):
                guard_x = i
                guard_y = j
                new_guard='v'
                down=True
            else :
                continue


            # movement logic
            if up:
                if (i==0):
                    guard_out = True
                else:
                    next_char = map[i-1][j]
                    if (next_char=="."):
                        new_guard_x = i-1
                        new_guard_y = j
                    if (next_char=="#"):
                        new_guard_x = i
                        new_guard_y = j
                        new_guard = '>'

            elif down:
                if (i==height-1):
                    guard_out = True
                else:
                    next_char = map[i+1][j]
                    if (next_char=="."):
                        new_guard_x = i+1
                        new_guard_y = j
                    if (next_char=="#"):
                        new_guard_x = i
                        new_guard_y = j
                        new_guard = '<'

            elif right:
                if (j==width-1):
                    guard_out = True
                else:
                    next_char = map[i][j+1]
                    if (next_char=="."):
                        new_guard_x = i
                        new_guard_y = j+1
                    if (next_char=="#"):
                        new_guard_x = i
                        new_guard_y = j
                        new_guard = 'v'

            elif left:
                if (j==0):
                    guard_out = True
                else:
                    next_char = map[i][j-1]
                    if (next_char=="."):
                        new_guard_x = i
                        new_guard_y = j-1
                    if (next_char=="#"):
                        new_guard_x = i
                        new_guard_y = j
                        new_guard = '^'


    
    # movement action
    map[guard_x][guard_y]="."
    map[new_guard_x][new_guard_y] = new_guard

    guard_pos = [new_guard_x, new_guard_y]
    if (guard_pos in traversed_path):
        pass
    else:
        traversed_path.append(guard_pos)



print(len(traversed_path))

fh.close()