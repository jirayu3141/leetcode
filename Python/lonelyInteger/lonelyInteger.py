#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # create a dictionary to store the number of occurrences of each number
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    # find the number that occurs only once
    for i in d:
        if d[i] == 1:
            return i

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()