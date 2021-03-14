ops = {
    "AND": "0000",
    "ADD": "0001",
    "LD": "0010",
    "ST": "0011",
    "ANDI": "0100",
    "ADDI": "0101",
    "CMP": "0110",
    "JUMP": "0111",
    "JE": "1000",
    "JA": "1001",
    "JB": "1010",
    "JBE": "1011",
    "JAE": "1100",
}

regs = {
    "R0": "000",
    "R1": "001",
    "R2": "010",
    "R3": "011",
    "R4": "100",
    "R5": "101",
    "R6": "110",
    "R7": "111",
}

def binary_digits(n, bits):
    s = bin(int(n) & int("1" * bits, 2))[2:]
    return ("{0:0>%s}" % bits).format(s)


lines = []
with open("input.txt") as f:
    for text in f.readlines():
        line = text.split()
        line.append(line[1].split(','))
        del line[1]
        lines.append(line)

hexadecimals = []
for x in lines:
    string = ops[x[0]]
    for r in x[1]:
        if r in regs:
            string += regs[r]
        else:
            len_of_ops = (16 - len(string))
            if int(ops[x[0]],2) >= int('0111',2):
                len_of_ops = 11
            string += binary_digits(r,len_of_ops)
    if len(string) < 16:
        string = string + '0' *(16 - len(string))
    hd = (len(string) + 3) // 4
    hex = '%.*x' % (hd, int('0b'+string, 0))
    hexadecimals.append(hex)
    print(string)

with open('instruction_memory.hex', 'w') as f:
    f.write('v2.0 raw\n')
    for ins in hexadecimals:
        f.write(("%s\n" % ins).upper())