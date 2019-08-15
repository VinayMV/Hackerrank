#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    minimum=min(arr)
    maximum=max(arr)
    count_max=count_min=sum_min=sum_max=0
    for i in arr:
        if i==minimum:
            if count_min>0:
                sum_min+=i
            else:
                count_min+=1
        if i==maximum: 
            if count_max>0:
                sum_max+=i
            else:
                count_max+=1
        if i>minimum:
            sum_max+=i
        if i<maximum:
            sum_min+=i
    print(sum_min,sum_max)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
