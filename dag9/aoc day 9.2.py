grootte = set()
def main():
    global grootte
    grootste3 = [0,0,0]
    matrix = []
    aantal = 0
    rij = []
    som = 0
    file = open("dag-9.txt", "r")
    for line in file.readlines():
        for getal in line:
            if getal != "\n":
                rij.append(int(getal))
        matrix.append(rij)
        rij = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_neighbors = neighbours(matrix, i, j)
            lowpoint = True
            for element in new_neighbors:
                if element <= matrix[i][j]:
                    lowpoint = False
            if lowpoint == True:
                grootte.add(str(i) + "," + str(j))
                findbassin(matrix, i, j)
                print(grootte)
                grootte.discard(0)
                aantal += 1
                lengte = len(grootte)
                print(len(grootte))
                if lengte > grootste3[0]:
                    grootste3[0] = lengte
                    if grootste3[0] > grootste3[1]:
                        grootste3[0], grootste3[1] = grootste3[1], grootste3[0]
                    if grootste3[1] > grootste3[2]:
                        grootste3[2], grootste3[1] = grootste3[1], grootste3[2]
                print(grootste3)
                grootte.clear()
    print(grootste3)
    print(aantal)
    print(grootste3[0] * (grootste3[1]) * grootste3[2])
def findbassin(matrix, i ,j):
    global grootte
    if matrix[i][j] == 9:
        return 0
    if i != 0:
        if matrix[i-1][j] == matrix[i][j] + 1 and matrix[i-1][j] != 9:
            grootte.add(str(i-1) + "," + str(j))
            findbassin(matrix ,i -1,j)
    if j != len(matrix[i]) - 1:
        if matrix[i][j+1] == matrix[i][j] + 1 and matrix[i][j+1] != 9:
            grootte.add(str(i) + "," + str(j + 1))
            findbassin(matrix, i, j+1)
    if i != len(matrix) - 1:
        if matrix[i+1][j] == matrix[i][j] + 1 and matrix[i+1][j] != 9:
            grootte.add(str(i + 1) + "," + str(j))
            findbassin(matrix, i + 1, j)
    if j != 0:
        if matrix[i][j-1] == matrix[i][j] + 1 and matrix[i][j-1] != 9:
            grootte.add(str(i) + "," + str(j-1))
            findbassin(matrix, i, j-1)
    #string = ""
    #string += str(i)
    #string += ","
    #string += str(j)
    #return string


def neighbours(matrix, i ,j):
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
            matrix[i][j - 1]  # left neighbor
    ]
    return new_neighbors
main()
#483664