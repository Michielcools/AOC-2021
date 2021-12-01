aantal = 0
vorigeline = 0
with open("dag-1.txt") as f:
    for line in f:
        if int(line) > vorigeline and vorigeline != 0:
            aantal += 1
        vorigeline = int(line)
print(aantal)
