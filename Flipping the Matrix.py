#     for a in range(q):
#         a = [[0 for j in range(2*q)] for i in range(2*q)]
        
#         for x in range(2*q):
#             c = [int(q) for q in input().strip().split('')]
#             a[x] = c
#         v = 0
#         for i in range(q):
#             for j in range(q):
#                 l = []
#                 l.append(a[i][j])
#                 l.append(a[2*q-1-i][j])
#                 l.append(a[i][2*q-1-j])
#                 l.append(a[2*q-1-i][2*n-1-j])
            
#                 maxv = max(l)
#                 v+= maxv
# return v

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here
    n = int(len(matrix) /  2)
    maxValue = 0
    total = 0
    
    for r in range(n):
        for c in range(n):
            maxValue += max(max(matrix[r][c],matrix[r][2*n-c-1]),
                            max(matrix[2*n-r-1][c],matrix[2*n-r-1][2*n-c-1]))
    return maxValue

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()