
def meestvoorkomende(matrix,pos):
    aantal1 = 0
    aantal0 = 0
    for line in matrix:
        if int(line[pos]) == 1:
            aantal1 += 1
        elif int(line[pos]) == 0:
            aantal0 += 1
    if aantal1 >= aantal0:
        return 1
    else:
        return 0
def minstvoorkomende(matrix,pos):
    aantal1 = 0
    aantal0 = 0
    for line in matrix:
        if int(line[pos]) == 1:
            aantal1 += 1
        elif int(line[pos]) == 0:
            aantal0 += 1
    if aantal1 < aantal0:
        return 1
    else:
        return 0
def verwijderrest(matrix, filter, pos):
    nieuwematrix = []
    for line in matrix:
        test = line[pos]
        if int(test) == filter:
            nieuwematrix.append(line)
    return nieuwematrix

def main():
    lijst =[]
    n = 0
    matrix = []
    filter = 0
    csrmatrix = []
    ogrmatrix = []
    file = open("dag-3.txt", "r")
    for line in file.readlines():
        matrix.append(line)
    while n < 12:
        filter = meestvoorkomende(matrix, n)
        matrix = verwijderrest(matrix, filter, n)
        if len(matrix) == 1:
            ogr = matrix[0]
            print(ogr)
            n += 12
        else:
            n += 1
    n = 0
    matrix = []
    file = open("dag-3.txt", "r")
    for line in file.readlines():
        matrix.append(line)
    while n < 12:
        filter = minstvoorkomende(matrix, n)
        matrix = verwijderrest(matrix, filter, n)
        print(matrix)
        if len(matrix) == 1:
            csr = matrix[0]
            print(csr)
            n += 12
        else:
            n += 1
    i = 0
    while i < 12:
        csrmatrix.append(int(csr[i]))
        i += 1
    i = 0
    while i < 12:
        ogrmatrix.append(int(ogr[i]))
        i += 1

    print(ogrmatrix)
    print(csrmatrix)
    csr = sum(val * (2 ** idx) for idx, val in enumerate(reversed(csrmatrix)))
    print(csr)
    ogr = sum(val * (2 ** idx) for idx, val in enumerate(reversed(ogrmatrix)))
    print(ogr)
    print(csr * ogr)


main()
#4474944