def main():
    file = open("dag-6.txt", "r")
    line = file.readline()
    newstr = ''.join((ch if ch in '0123456789' else ' ') for ch in line)
    gegeven = [int(i) for i in newstr.split()]
    dagen = 0
    aantal = 0
    vissen = [0,0,0,0,0,0,0,0,0]
    for i in gegeven:
        vissen[i] += 1
    while dagen <= 255:
        nieuwevissen = [0,0,0,0,0,0,0,0,0]
        for k in range(len(vissen)):
            aantal = vissen[k]
            if k == 0:
                nieuwevissen[8] += aantal
                nieuwevissen[6] += aantal
            else:
                nieuwevissen[k-1] += aantal
        vissen = nieuwevissen
        dagen += 1
    print(sum(vissen))

main()