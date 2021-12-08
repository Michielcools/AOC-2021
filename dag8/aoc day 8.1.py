def main():
    aantaluniek = 0
    file = open("dag-8.txt", "r")
    for line in file.readlines():
        lijst = line.split()
        output = lijst[-4:]
        for getal in output:
            if len(getal) == 2 or len(getal) == 3 or len(getal) == 4 or len(getal) == 7:
                aantaluniek += 1
    print(aantaluniek)


main()
