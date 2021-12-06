def main():
    file = open("dag-6.txt", "r")
    line = file.readline()
    newstr = ''.join((ch if ch in '0123456789' else ' ') for ch in line)
    gegeven = [int(i) for i in newstr.split()]
    dagen = 0
    nieuwgegeven = gegeven
    while dagen <= 79:
        for vis in range(len(gegeven)):
            if gegeven[vis] == 0:
                nieuwgegeven[vis] = 6
                nieuwgegeven.append(8)
            else:
                nieuwgegeven[vis] -= 1
        gegeven = nieuwgegeven
        dagen += 1
    print(len(gegeven))
main()