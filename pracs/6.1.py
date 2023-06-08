def xbase(x, left, right):
    if x[3] == "XBASE":
        return left
    else:
        return right


def abap(x, left, middle, right):
    if x[1] == "ABAP":
        return left
    elif x[1] == "CSV":
        return middle
    else:
        return right


def numpy(x, left, right):
    if x[2] == "NUMPY":
        return left
    else:
        return right


def main(x):
    if x[4] == 1975:
        return xbase(x, abap(x, numpy(x, 0, 1), numpy(x, 2, 3), numpy(x, 4, 5)), 6)
    elif x[4] == 2016:
        return numpy(x, abap(x, 8, xbase(x, 9, 10), 11), 12)
    else:
        return 7


print(main(['LUA', 'EC', 'NUMPY', 'ASN.1', 1975]))
print(main(['JSON5', 'CSV', 'AWK', 'ASN.1', 2016]))
print(main(['JSON5', 'EC', 'NUMPY', 'XBASE', 2016])) 
print(main(['ORG', 'ABAP', 'NUMPY', 'ASN.1', 2016])) 
print(main(['LUA', 'CSV', 'NUMPY', 'XBASE', 1973]))