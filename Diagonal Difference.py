#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    sum_primary=sum_secondary=0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i==j:
                sum_primary+=arr[i][j]
            if i+j==(len(arr)-1):
                sum_secondary+=arr[i][j]
    return(abs(sum_secondary-sum_primary))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
