#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    price_actual=0
    for i in range(len(bill)):
        if i != k:
            price_actual+=bill[i]
    price_actual=int(price_actual/2)
    if b==int(price_actual):
        print("Bon Appetit")
    else:
        print(b-price_actual)


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
