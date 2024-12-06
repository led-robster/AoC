import math
import random


def middle_in_list(list):
    return int(list[math.floor(len(list)/2)])

fh = open("source.txt",'r')

ordering_dict = {}
seq_list = []
part1 = True
part2 = False

while (line := fh.readline()):
    line_stripped = line.strip()

    if (line=="\n"):
        part1 = False
        part2 = True
        continue

    if (part2):
        seq_list.append(line_stripped)

    if (part1):
        line_list = line_stripped.split('|')
        if (line_list[0] in ordering_dict):
            ordering_dict[line_list[0]].append(line_list[1])
        else:
            ordering_dict[line_list[0]] = [line_list[1]]

print("1. file parsed.")

wrong = False
correct_eq_list = []
no_correct_eq_list = []

for seq in seq_list:
    wrong = False
    num_list = seq.split(',')
    for idx in range(len(num_list)-1,-1,-1):
        if (idx==0):
            continue
        if (num_list[idx] in ordering_dict):
            for jdx in range(idx,-1,-1):
                if (num_list[jdx] in ordering_dict[num_list[idx]]):
                    # not correct order
                    wrong = True

    if (not wrong):
        correct_eq_list.append(seq)
    else :
        no_correct_eq_list.append(seq)


part1_sum =0

for seq in correct_eq_list:
    num_list = seq.split(',')
    part1_sum += middle_in_list(num_list)
    pass

print("part1 completed.")
print("no. of NOT corrected sequences: " + str(len(no_correct_eq_list)))

new_correct_seq_list = []
corrected = False
part2_cnt = 0

for seq in no_correct_eq_list:

    part2_cnt +=1
    if (part2_cnt==10):
        print("part2 @ 10.")
    elif (part2_cnt==50):
        print("part2 @ 50")
    elif (part2_cnt==100):
        print("part2 @ 100")

    wrong=False
    corrected = False
    num_list = seq.split(',')

    while (not corrected):
        for idx in range(len(num_list)-1,-1,-1):
            if (idx==0):
                    continue
            else :
                if (num_list[idx] in ordering_dict):
                    for jdx in range(idx,-1,-1):
                        if (num_list[jdx] in ordering_dict[num_list[idx]]):
                            # not correct order
                            wrong = True
                            break
                
                if (wrong):
                    break

        if (not wrong):
            wrong = False
            corrected = True
            new_correct_seq_list.append(num_list)
        else:
            value = num_list.pop(idx)
            num_list.insert(jdx, value)
            wrong = False
            corrected = False
            


part2_sum =0

for seq in new_correct_seq_list:
    part2_sum += middle_in_list(seq)
    pass

print(part2_sum)

fh.close()