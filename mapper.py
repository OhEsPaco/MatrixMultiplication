#!/usr/bin/env python

import sys


def printOutput(row, col, values):
    key = ",".join([row, col])
    value = ",".join(values)
    print("{}\t{}".format(key, value))

# Diccionario para guardar las matrices
matrixDictionary = dict()
# Diccionario para guardar las dimensiones de las matrices
rowColsDictionary = dict()

# Se parsean desde el archivo
for line in sys.stdin:
    line = line.strip()
    keys = line.split('\n')

    for key in keys:
        lineKeys = line.split(',')
        if len(lineKeys) != 4:
            raise Exception("Invalid input file")

        if lineKeys[0] not in matrixDictionary:
            matrixDictionary[lineKeys[0]] = []
            rowColsDictionary[lineKeys[0]] = [int(lineKeys[1]), int(lineKeys[2])]

        if lineKeys[0] in rowColsDictionary and rowColsDictionary[lineKeys[0]][0] < int(lineKeys[1]):
            rowColsDictionary[lineKeys[0]][0] = int(lineKeys[1])

        if lineKeys[0] in rowColsDictionary and rowColsDictionary[lineKeys[0]][1] < int(lineKeys[2]):
            rowColsDictionary[lineKeys[0]][1] = int(lineKeys[2])

        matrixDictionary[lineKeys[0]].append([int(lineKeys[1]), int(lineKeys[2]), int(lineKeys[3])])

parsedMatrixDictionary = []
index = 0
# Se construyen las matrices
for key in matrixDictionary:
    rows = rowColsDictionary[key][0] + 1
    cols = rowColsDictionary[key][1] + 1
    data = matrixDictionary[key]
    parsedMatrixDictionary.append([[0 for col in range(cols)] for row in range(rows)])
    for rawData in data:
        parsedMatrixDictionary[index][rawData[0]][rawData[1]] = rawData[2]
    index += 1

if len(parsedMatrixDictionary) != 2:
    raise Exception("Only too matrix are needed")

result = []
for i in range(len(parsedMatrixDictionary[0])):
    for j in range(len(parsedMatrixDictionary[1])):
        result = []
        for k in range(len(parsedMatrixDictionary[1])):
            result.append(str(parsedMatrixDictionary[0][i][k]))
            result.append(str(parsedMatrixDictionary[1][k][j]))
        printOutput(str(i), str(j), result)

