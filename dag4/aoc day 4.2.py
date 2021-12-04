def main():
    file = open("dag-4.txt", "r")
    treknummers = []
    nummer = ""
    getallen = file.readline()
    for char in getallen:
        if char != ",":
            nummer += char
        else:
            treknummers.append(int(nummer))
            nummer = ""
    treknummers.append(int(nummer))
    n = 0
    m = 0
    bingokaart = []
    speler = []
    lijn = []
    tijdgetal = ""
    for line in file.readlines():
        if n != 0:
            for getal in line:
                if getal != " ":
                    tijdgetal += getal
                else:
                    if tijdgetal != "":
                        lijn.append(int(tijdgetal))
                    tijdgetal = ""
            lijn.append(int(tijdgetal))
            tijdgetal = ""
            n += 1
        else:
            n += 1
        if lijn != []:
            speler.append(lijn)
        if n == 6:
            bingokaart.append(speler)
            n = 0
            speler = []
        lijn = []
    winnaar = 0
    getrnummer = 0
    while len(bingokaart) != 1:
        getrnummer = treknummers[m]
        bingokaart = filternummer(bingokaart, getrnummer)
        bingokaart = controleerwinnaar(bingokaart)
        m += 1
    while winnaar == 0:
        getrnummer = treknummers[m]
        bingokaart = filternummer(bingokaart,getrnummer)
        winnaar = controleerwinnaartoteinde(bingokaart)
        m += 1
    score = berekenscore(bingokaart,0,getrnummer)
    print(score)

def filternummer(bingokaart, nummer):
    for spelernr in range(len(bingokaart)):
        for lijnnr in range(len(bingokaart[spelernr])):
            for getalnr in range(len(bingokaart[spelernr][lijnnr])):
                if bingokaart[spelernr][lijnnr][getalnr] == nummer:
                    bingokaart[spelernr][lijnnr][getalnr] = -1
    return(bingokaart)

def controleerwinnaar(bingokaart):
    topop = []
    aantalpops = 0
    for spelernr in range(len(bingokaart)):
        for rijnr in range(len(bingokaart[spelernr])):
            if bingokaart[spelernr][rijnr][0] == -1 and bingokaart[spelernr][rijnr][1] == -1 and bingokaart[spelernr][rijnr][2] == -1 and bingokaart[spelernr][rijnr][3] == -1 and bingokaart[spelernr][rijnr][4] == -1:
                if spelernr not in topop:
                    topop.append(spelernr)
        getalnr = 0
        while getalnr < 5:
            if bingokaart[spelernr][0][getalnr] == -1 and bingokaart[spelernr][1][getalnr] == -1 and bingokaart[spelernr][2][getalnr] == -1 and bingokaart[spelernr][3][getalnr] == -1 and bingokaart[spelernr][4][getalnr] == -1:
                if spelernr not in topop:
                    topop.append(spelernr)
                getalnr += 1
            else:
                getalnr += 1
    topop.sort()
    for i in topop:
        bingokaart.pop(i-aantalpops)
        aantalpops += 1
    return bingokaart
def controleerwinnaartoteinde(bingokaart):
    for spelernr in range(len(bingokaart)):
        for rijnr in range(len(bingokaart[spelernr])):
            if bingokaart[spelernr][rijnr][0] == -1 and bingokaart[spelernr][rijnr][1] == -1 and bingokaart[spelernr][rijnr][2] == -1 and bingokaart[spelernr][rijnr][3] == -1 and bingokaart[spelernr][rijnr][4] == -1:
                return 1
        getalnr = 0
        while getalnr < 5:
            if bingokaart[spelernr][0][getalnr] == -1 and bingokaart[spelernr][1][getalnr] == -1 and bingokaart[spelernr][2][getalnr] == -1 and bingokaart[spelernr][3][getalnr] == -1 and bingokaart[spelernr][4][getalnr] == -1:
                return 1
            else:
                getalnr += 1
    return 0
def berekenscore(bingokaart, winnaar,nummer):
    score = 0
    for rij in bingokaart[winnaar]:
        for getal in rij:
            if getal != -1:
                score += getal
    score *= nummer
    return score
main()
