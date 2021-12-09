def main():
    matrix = []
    rij = []
    som = 0
    aantal = 0
    file = open("dag-9.txt", "r")
    for line in file.readlines():
        for getal in line:
            if getal != "\n":
                rij.append(int(getal))
        matrix.append(rij)
        rij = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == 0 or i == len(matrix) - 1 or j == 0 or j == len(matrix[i]) - 1:
                new_neighbors = []
                if i != 0:
                    new_neighbors.append(matrix[i - 1][j])  # top neighbor
                if j != len(matrix[i]) - 1:
                    new_neighbors.append(matrix[i][j + 1])  # right neighbor
                if i != len(matrix) - 1:
                    new_neighbors.append(matrix[i + 1][j])  # bottom neighbor
                if j != 0:
                    new_neighbors.append(matrix[i][j - 1])
            else:
                new_neighbors = [
                    matrix[i - 1][j],  # top neighbor
                    matrix[i][j + 1],  # right neighbor
                    matrix[i + 1][j],  # bottom neighbor
                    matrix[i][j - 1]   # left neighbor
                ]
            lowpoint = True
            for element in new_neighbors:
                if element <= matrix[i][j]:
                    lowpoint = False
            if lowpoint == True:
                som += (matrix[i][j] + 1)
                aantal += 1
    print(som)
    print(aantal)


main()
