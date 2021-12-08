import collections
def main():
    som = 0
    einde = ""
    file = open("dag-8.txt", "r")
    for line in file.readlines():
        lijst = line.split()
        input = lijst[:10]
        code = bepaal_posities(input)
        output = lijst[-4:]
        for getal in output:
            if collections.Counter(getal) == collections.Counter(code[0]):
                einde += "0"
            elif collections.Counter(getal) == collections.Counter(code[1]):
                einde += "1"
            elif collections.Counter(getal) == collections.Counter(code[2]):
                einde += "2"
            elif collections.Counter(getal) == collections.Counter(code[3]):
                einde += "3"
            elif collections.Counter(getal) == collections.Counter(code[4]):
                einde += "4"
            elif collections.Counter(getal) == collections.Counter(code[5]):
                einde += "5"
            elif collections.Counter(getal) == collections.Counter(code[6]):
                einde += "6"
            elif collections.Counter(getal) == collections.Counter(code[7]):
                einde += "7"
            elif collections.Counter(getal) == collections.Counter(code[8]):
                einde += "8"
            elif collections.Counter(getal) == collections.Counter(code[9]):
                einde += "9"
        som += int(einde)
        einde = ""
    print(som)


def bepaal_posities(input):
    mt = set()
    lbt = set()
    rbt = set()
    rot = set()
    for getal in input:
        if len(getal) == 2:
            a1 = getal
        if len(getal) == 3:
            a7 = getal
        if len(getal) == 4:
            a4 = getal
        if len(getal) == 7:
            a8 = getal
    for x in a7:
        if x not in a1:
            b = x
    for x in a1:
        rbt.add(x)
        rot.add(x)
    for x in a4:
        if x not in a1:
            mt.add(x)
            lbt.add(x)
    for getal in input:
        for x in rbt:
            if len(getal) == 6 and x not in getal:
                rb = x
                a6 = getal
        for x in mt:
            if len(getal) == 6 and x not in getal:
                m = x
                a0 = getal
    for x in rot:
        if x != rb:
            ro = x
    for x in lbt:
        if x != m:
            lb = x
    for getal in input:
        if len(getal) == 6 and getal != a6 and getal != a0:
            a9 = getal
        if len(getal) == 5:
            if rb not in getal:
                a5 = getal
            elif ro not in getal:
                a2 = getal
            else:
                a3 = getal
    getallen = []
    getallen.append(a0)
    getallen.append(a1)
    getallen.append(a2)
    getallen.append(a3)
    getallen.append(a4)
    getallen.append(a5)
    getallen.append(a6)
    getallen.append(a7)
    getallen.append(a8)
    getallen.append(a9)
    return getallen




main()