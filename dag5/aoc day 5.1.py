def main():
    matrix = []
    rij = []
    i = 0
    while i < 1000:
        j = 0
        while j < 1000:
            rij.append(0)
            j += 1
        matrix.append(rij)
        rij = []
        i += 1
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    xteller = 0
    yteller = 0
    file = open("dag-5.txt", "r")
    for line in file.readlines():
        newstr = ''.join((ch if ch in '0123456789' else ' ') for ch in line)
        listOfNumbers = [int(i) for i in newstr.split()]
        x1 = listOfNumbers[0]
        y1 = listOfNumbers[1]
        x2 = listOfNumbers[2]
        y2 = listOfNumbers[3]
        if x1 == x2:
            if y2 >= y1:
                yteller = y1
                while yteller <= y2:
                    matrix[yteller][x1] += 1
                    yteller += 1
            elif y1 > y2:
                yteller = y2
                while yteller <= y1:
                    matrix[yteller][x1] += 1
                    yteller += 1
        elif y1 == y2:
            if x1 <= x2:
                xteller = x1
                while xteller <= x2:
                    matrix[y1][xteller] += 1
                    xteller += 1
            elif x2 < x1:
                xteller = x2
                while xteller <= x1:
                    matrix[y1][xteller] += 1
                    xteller += 1
    aantaldubbels = 0
    for rij in matrix:
        for getal in rij:
            if getal >= 2:
                aantaldubbels += 1
    print(aantaldubbels)




main()