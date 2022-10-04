#!/usr/bin/env python
# Pascal's triangle using python

import numpy as np

def triangle(rows) :
    A = np.zeros( (rows,rows),dtype=int ) # integer matrix
    for j in range (0, rows) :
        A[j][0] = 1
        for k in range (0, rows) :
            if k != 0 and j != 0 :
                A[j][k] = A[j-1][k]+A[j-1][k-1]
    return A
###############################################


#################################################

rows = int(input('Enter how many rows to show: '))
print(triangle(rows))


# same but without numpy and matrix
def printPascal(N):
    arr = [1]
    temp = []
    print("pascal's triangle of", N, "Rows ...")
    for i in range(N) :
        print("rows", i+1, end=" : ")
        for j in range(len(arr)) :
            print(arr[j], end='') # end = '' means no new line
        print() # print end of line
        temp.append(1)

        for j in range(len(arr)-1) :
            temp.append(arr[j] + arr[j + 1])
        temp.append(1)
        arr = temp
        temp = []
N = rows
printPascal(N)
