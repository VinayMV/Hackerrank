#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    hour=int(s[0:2])
    minute=(s[3:5])
    sec=(s[6:8])
    time=s[8:len(s)]
    new_hour=''
    if time=='PM':
        if hour<12:
            new_hour+=str(hour+12)
        elif hour==12:
            new_hour+=str(hour)
    elif time=='AM':
        if hour==12:
            new_hour+="00"
        else:
            new_hour+=s[0:2]
    new_hour+=":"+str(minute)+":"+str(sec)
    return(new_hour)
    #

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
