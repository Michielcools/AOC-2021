def main():
    file = open("dag-7.txt", "r")
    line = file.readline()
    newstr = ''.join((ch if ch in '0123456789' else ' ') for ch in line)
    gegeven = [int(i) for i in newstr.split()]
    i = 0
    lijst = []
    laagstesom = 9999999999
    bestei= 0
    while i < 2000:
        for k in gegeven:
            verschil = k - i
            verschil = abs(verschil)
            lijst.append(verschil)
        som = sum(lijst)
        i += 1
        if som < laagstesom:
            laagstesom = som
            bestei = i - 1
        lijst = []
    print(laagstesom, bestei)
main()