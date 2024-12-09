
def check_result(int_operands, result):
    num_operators = len(int_operands)-1
    for i in range(0, (2**num_operators)-1):
        bin_str = bin(i).split('b')[1]
        for idx in range(0,len(bin_str)):
            if (bin_str=='1'):
                int_operands[idx] * int_operands[idx+1]

fh = open("test.txt", 'r')

while (line := fh.readline()):
    line_stripped = line.strip()
    line_splitted = line_stripped.split(':')
    result = int(line_splitted[0])
    line_operands = line_splitted[1].split()
    int_operands = [int(el) for el in line_operands]