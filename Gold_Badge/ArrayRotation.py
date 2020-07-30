# Perform Rotation on array
# This is working but failing the time limitation
# need to optimize for time
# Date : 13/07/2010  Optimized now :
# -------------------------------------------------------

import math
import random
import re
import sys
import os

# Complete the rotLeft function below.
def rotRight(aa, dd):
    # This works perfectly fine but complexity was bad
    for i in range(dd):
        print(i)
        nn = len(aa) - 1
        temp = aa[nn]
        for j in range(nn, 0, -1):
            aa[j] = aa[j - 1]
        aa[0] = temp
        print(i, aa)

# -----------------------------------------------
def rotLeft_done(aa, dd):
    # This works perfectly fine but complexity was bad
    for i in range(dd):
        nn = len(aa) - 1
        temp = aa[0]
        for j in range(0, nn):
            aa[j] = aa[j + 1]
        aa[nn] = temp
    print(aa, end="")
    return aa
# -----------------------------------------------
def rotLeft(aa, dd):
    # Improved Complexity
    n = len(aa)
    temp = [0] * n   # [0, 0, 0, 0, 0]
    for i in range(0, n):
        j = i + dd
        if j >= n:
            j = j - n
        temp[i] = aa[j]
    for i in temp:
        print(i, end=" ")


if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))
    result = rotLeft(a, d)
    #print(result)


