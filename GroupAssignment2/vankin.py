#!/usr/bin/python
maximum = 0
import sys
sys.setrecursionlimit(1000000)

def readInput(x,y):
    input_file = open("input.txt", "r")

    lines = input_file.readlines()  # store all lines

    row = lines[x+1].split(',')   #break up first line of ints
    #first
    return int(row[y])
    input_file.close()


def printMatrix(matrix):
    for i in range(0, len(matrix)):
        print(matrix[i])


def greatestPath(n):
    VMile = [[-1 for x in range(n)] for y in range(n)]
    maxscore = 0

    VMile.append([])
    # fill far right column with 0's
    for i in range(n - 1, -1, -1):
        VMile[i].append(0)
        VMile[n].append(0)
    VMile[n].append(0)
    # makes bottom square of current column 0 so we can check VMile[i][j+1]
    for j in range(n - 1, -1, -1):
        VMile[n][j] = 0

        for i in range(n - 1, -1, -1):
            VMile[i][j] = readInput(i, j) + max(VMile[i+1][j], VMile[i][j+1])
            maxscore = max(maxscore, VMile[i][j])

    return maxscore


def greatestPathRecursive(x, y, n, mem):

    global maximum
    if mem[x][y] == -1:
        for i in range(n-1, -1, -1):
            mem[i][y] = readInput(i, y) + max(greatestPathRecursive(i+1, y, n, mem), greatestPathRecursive(i, y + 1, n, mem))
            if mem[i][y] > maximum:
                maximum = max(maximum, mem[i][y])
    return mem[x][y]


def recursiveOuterLoop(n):
    mem = [[-1 for x in range(n + 1)] for y in range(n + 1)]
    for i in range(0, n + 1):
        mem[i][n] = 0
        mem[n][i] = 0

    for i in range(n - 1, -1, -1):
        greatestPathRecursive(i, i, n, mem)
    print(maximum)


input_file = open("input.txt", "r")
n = int(input_file.readline())
print(n)
# recursiveOuterLoop(n)

f = open("output.txt", "w+")
f.write(str(recursiveOuterLoop(n)))
exit(0)
