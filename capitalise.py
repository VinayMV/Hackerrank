#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s1=''
    s1+=s[0].upper()
    for i in range(1,len(s)):
        ch=s[i]
        try:
            if s[i-1]==' ':
                continue
            if ch==' ':
                s1+=ch
                s1+=s[i+1].upper()
            else:
                s1+=ch
        except:
            a=2
    return(s1)
        


if __name__ == '__main__':
