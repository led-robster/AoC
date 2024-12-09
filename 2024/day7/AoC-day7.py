import time



def concat(op1, op2):
    if (op2<10):
        op2_digit = 1
    elif (op2<100):
        op2_digit=2
    elif (op2<1000):
        op2_digit = 3
    elif (op2<10000):
        op2_digit = 4

    return op2+op1*(10**op2_digit)


def decimal_to_ternary(decimal_number, length):
    """
    Converts a decimal number to a ternary string of a specified length.

    :param decimal_number: int, the decimal number to convert.
    :param length: int, the desired length of the ternary string.
    :return: str, the ternary string of the specified length.
    """
    if decimal_number < 0:
        raise ValueError("The decimal number must be non-negative.")
    
    # Convert to ternary
    ternary_digits = []
    while decimal_number > 0:
        ternary_digits.append(str(decimal_number % 3))
        decimal_number //= 3
    
    ternary_string = ''.join(reversed(ternary_digits))  # Reverse to get the correct order
    return ternary_string.zfill(length)  # Pad with zeros to the specified length



def part1_check_result(int_operands, result):
    num_operators = len(int_operands)-1
    calculated = 0
    for i in range(0, (2**num_operators)):
        calculated = 0
        bin_str = bin(i).split('b')[1].zfill(num_operators)
        first_term = int_operands[0]*int_operands[1] if (bin_str[0]=='1') else int_operands[0]+int_operands[1] 
        calculated += first_term
        for idx in range(1,len(bin_str)):
            if (bin_str[idx]=='1'):
                calculated *= int_operands[idx+1]
            else:
                calculated += int_operands[idx+1]
                
        if (calculated==result):
            return True
    
    return False


def part2_check_result(int_operands, result):
    num_operators = len(int_operands)-1
    calculated = 0
    for i in range(0, (3**num_operators)):
        calculated = 0
        first_term=0
        tern_str = decimal_to_ternary(i,num_operators)
        if (tern_str[0]=='1'):
            first_term = int_operands[0]*int_operands[1]
        elif (tern_str[0]=='0'):
            first_term = int_operands[0]+int_operands[1]
        elif (tern_str[0]=='2'):
            first_term = concat(int_operands[0], int_operands[1])

        calculated += first_term
        for idx in range(1,len(tern_str)):
            if (tern_str[idx]=='1'):
                calculated *= int_operands[idx+1]
            elif (tern_str[idx]=='2'):
                calculated = concat(calculated, int_operands[idx+1])
            else:
                calculated += int_operands[idx+1]
                
        if (calculated==result):
            return True
    
    return False


fh = open("source.txt", 'r')

part1_cnt = 0
part2_cnt = 0

start_time = time.time()

while (line := fh.readline()):
    line_stripped = line.strip()
    line_splitted = line_stripped.split(':')
    result = int(line_splitted[0])
    line_operands = line_splitted[1].split()
    int_operands = [int(el) for el in line_operands]
    if (part1_check_result(int_operands, result)):
        part1_cnt+=result
    else:
        pass

part1_time = time.time()

print("part 1: " + str(part1_cnt))
print("elapsed time: " + str(part1_time-start_time))

start2_time = time.time()

fh.close()

fh = open("source.txt",'r')

while (line := fh.readline()):
    line_stripped = line.strip()
    line_splitted = line_stripped.split(':')
    result = int(line_splitted[0])
    line_operands = line_splitted[1].split()
    int_operands = [int(el) for el in line_operands]
    if (part2_check_result(int_operands, result)):
        part2_cnt+=result
    else:
        pass


part2_time = time.time()

print("part 2: " + str(part2_cnt))
print("elapsed time: "+ str(part2_time-start2_time))


fh.close()