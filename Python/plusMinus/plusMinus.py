#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # count the number of positive, negative and zero numbers
    pos = 0
    neg = 0
    zero = 0
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zero += 1

    # calculate the ratio of positive, negative and zero numbers
    pos_ratio = pos / len(arr)
    neg_ratio = neg / len(arr)
    zero_ratio = zero / len(arr)

    # print the ratio of positive, negative and zero numbers (limit to 6 decimal places)
    print(f"{pos_ratio:.6f}")
    print(f"{neg_ratio:.6f}")
    print(f"{zero_ratio:.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
