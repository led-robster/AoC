import time


def leftmost_free(list):
    for idx in range(0,len(list)):
        if list[idx]=='.':
            return idx
        
def rightmost_block(list):
    for idx in range(len(list)-1,-1,-1):
        if list[idx]!='.':
            return idx
        
def swap_indices(lst, index1, index2):
    # Swap the elements at index1 and index2
    lst[index1], lst[index2] = lst[index2], lst[index1]

def checksum(list):
    checksum = 0
    for idx in range(0, len(list)):
        if (list[idx]=="."):
            continue
        checksum += idx*list[idx]

    return checksum

fh = open("source.txt", 'r')

while (line := fh.readline()):
    stripped = line.strip()
    output_list = []
    id = 0
    for idx in range(0, len(stripped), 2):
        for iter in range(0,int(stripped[idx])):
            output_list.append(id)

        if (idx+1==len(stripped)):
            # out of range
            break
        if (int(stripped[idx+1])==0):
            pass
        else:
            for iter in range(0,int(stripped[idx+1])):
                output_list.append('.')

        id = id+1
        
fh.close()

# print(output_list)
copy_list = list(output_list)

ordered = False

start_time = time.time()

while (not ordered):
    leftmost_free_idx = leftmost_free(output_list)
    rightmost_block_idx = rightmost_block(output_list)
    swap_indices(output_list, leftmost_free_idx, rightmost_block_idx)
    
    lf_idx_star = leftmost_free(output_list)
    rb_idx_star = rightmost_block(output_list)

    if (lf_idx_star==rb_idx_star+1):
        ordered = True

print("completed ordering.")

end_time = time.time()
#print("ordered string: " + new_string)
delta_time = end_time-start_time
print(f"elapsed time : {delta_time:.2f}")

print("checksum : " + str(checksum(output_list)))

## PART2
##-----------------------------------------------------------------------

def rightmost_file_block(list, number):
    found_value = -1
    right_index = 0
    left_index = 0
    for idx in range(len(list)-1,-1,-1):
        if (list[idx]=='.'):
            if found_value==1:
                left_index = idx+1
                break
            else:
                continue
        else:
            if found_value==-1:
                if list[idx]==number:
                    found_value = 1
                    right_index = idx

                continue
            else:
                if list[idx]!=number:
                    left_index = idx+1
                    break

    return right_index, left_index

def leftmost_empty_block(list, size):
    found = False
    start_idx=0
    end_idx=0
    for idx in range(0,len(list)):
        if not found:
            if list[idx]=='.':
                start_idx = idx
                found = True
        else:
            if list[idx]!='.':
                end_idx = idx-1
                if end_idx-start_idx+1<size:
                    found=False
                    start_idx=-1
                    end_idx=-1
                    continue
                else :
                    block=True
                    break

    return start_idx, end_idx

def swap_blocks(lst, start1, end1, start2, end2):
    # Ensure valid indices
    if start1 < 0 or start2 < 0 or end1 >= len(lst) or end2 >= len(lst) or start1 > end1 or start2 > end2:
        raise ValueError("Invalid block indices")

    # Extract the blocks
    block1 = lst[start1:end1 + 1]
    block2 = lst[start2:end2 + 1]

    # Handle the case where blocks overlap
    if start2 > end1:  # No overlap
        lst[start1:end1 + 1] = block2
        lst[start2:end2 + 1] = block1
    else:  # Blocks overlap; temporary storage needed
        temp = block1
        lst[start1:end1 + 1] = block2
        lst[start2:end2 + 1] = temp

    return lst


new_start_time = time.time()

for file_id in range(copy_list[-1],0,-1):
    right_ix, left_ix = rightmost_file_block(copy_list, file_id)
    block_size = right_ix-left_ix+1
    start_ix, end_ix = leftmost_empty_block(copy_list, block_size)

    if (start_ix==-1 or end_ix==-1 or right_ix<start_ix):
        continue

    empty_size = end_ix-start_ix+1

    if block_size<=empty_size:
        copy_list = swap_blocks(copy_list, left_ix, right_ix, start_ix, end_ix-(empty_size-block_size))


new_stop_time = time.time()

new_delta_time = new_stop_time-new_start_time

print("part 2 ordering : ")
# print(copy_list)
print("part 2 checksum : " + str(checksum(copy_list)))
print(f"part 2 elapsed time : {new_delta_time:.2f}")

