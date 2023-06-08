def x1(x, k):
    if x[1] == "JAVA":
        return k
    else:
        k += 1
        return k


def main(x):
    k = 4
    if x[0] == 1963:
        if x[3] == 'EDN':
            if x[2] == "FANCY":
                return 0
            elif x[2] == "ASN.1":
                return 1
            else:
                return 2
        elif x[3] == 'SMALI':
            return 3
        else:
            return x1(x, k)
    elif x[0] == 1957:
        k = 6
        return x1(x, k)
    else:
        if x[3] == "EDN":
            return 8
        elif x[3] == "SMALI":
            k = 9
            return x1(x, k)
        else:
            return 11

print(main([1957, 'NIT', 'SMALI', 'EDN']))
            