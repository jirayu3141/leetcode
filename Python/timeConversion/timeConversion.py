#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # extract last two characters
    am_pm = s[-2:]
    # if the last two characters are "AM"
    if am_pm == "AM":
        return s[:-2]
    # if the last two characters are "PM"
    else:
        # extract the first two integers
        hour = int(s[:2]) + 12
        # if the hour is 24
        if hour >= 24:
            hour -= 12
        
        # replace first two characters with the hour
        return str("{:02d}".format(hour)) + s[2:-2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    print(result)

    fptr.write(result + '\n')

    fptr.close()
