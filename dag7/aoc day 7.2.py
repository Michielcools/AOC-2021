def main():
    file = open("dag-7.txt", "r")
    line = file.readline()
    newstr = ''.join((ch if ch in '0123456789' else ' ') for ch in line)
    gegeven = [int(i) for i in newstr.split()]
    i = round(sum(gegeven)/len(gegeven))
    lijst = []
    for k in gegeven:
        verschil = abs(k - i)
        lijst.append(recsom(verschil))
    print(sum(lijst))
def recsom(getal):
    i = 1
    som = 0
    while i <= getal:
        som += i
        i += 1
    return(som)
main()