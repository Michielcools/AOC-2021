aantal = 0
line2 = 0
line3 = 0
vorigesom = 0
with open("dag-1.txt") as f:
    for line in f:
        som1 = int(line) + int(line2) + int(line3)
        if som1 > vorigesom and vorigesom != 0 and line3 != 0:
            aantal += 1
        if line3 != 0:
            vorigesom = som1
        line3 = line2
        line2 = line
print(aantal)
