def main(x):
    e1 = bin(int(x[0]) & 127)[2:]
    while len(e1) != 7:
        e1 = "0" + e1
    e2 = "00000"
    e3 = bin(int(x[1]) & 63)[2:]
    while len(e3) != 6:
        e3 = "0" + e3
    e4 = bin(int(x[2]) & 63)[2:]
    while len(e4) != 6:
        e4 = "0" + e4
    e5 = bin(int(x[3]) & 3)[2:]
    res = "0b" + e5 + e4 + e3 + e2 + e1
    return (int(res, 2))


print(main(('112', '22', '43', '0')))