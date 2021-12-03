aantal1 = 0
aantal0 = 0
lijst =[]
n = 0
while n < 12:
    file = open("dag-3.txt", "r")
    for line in file.readlines():
        test = line[n]
        if int(line[n]) == 1:
            aantal1 += 1
        elif int(line[n]) == 0:
            aantal0 += 1
    if aantal1 > aantal0:
        lijst.append(1)
    else:
        lijst.append(0)
    n += 1
    aantal1 = 0
    aantal0 = 0
print(lijst)
anderelijst = []
for nr in lijst:
    if nr == 0:
        anderelijst.append(1)
    else:
        anderelijst.append(0)
string1 = ""
string2 = ""
a = 0
getal1 = sum(val*(2**idx) for idx, val in enumerate(reversed(lijst)))
getal2 = sum(val*(2**idx) for idx, val in enumerate(reversed(anderelijst)))
print(getal1*getal2)
