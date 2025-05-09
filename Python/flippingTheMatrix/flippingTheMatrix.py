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

# 1 2  3  4
# 5 6  7  8
# 9 10 11 12

# n = 2

def flippingMatrix(matrix):
    # Write your code here
    n = len(matrix) // 2
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += max(matrix[i][j], matrix[i][2*n-1-j], matrix[2*n-1-i][j], matrix[2*n-1-i][2*n-1-j])
    return sum





if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)
        print(result)

        # fptr.write(str(result) + '\n')

    # fptr.close()