#!/bin/python3
# Medium - Worked like charm
# Binary search helped in improving the complexity
# ---------------------------------- #
import math
import os
import random
import re
import sys

# Complete the pairs function below.
def binary_search(ar, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if ar[mid] < x:
            low = mid + 1
        elif ar[mid] > x:
            high = mid - 1
        else:
            return 1
    return 0
def pairs(kk, ar):
    count = 0
    ar = sorted(ar)
    for i in range(len(ar)):
        print(f"i = {i}")
        temp = ar[i]+kk
        if binary_search(ar, temp):
            count += 1
    return count


if __name__ == '__main__':
    fptr = open('pairs', 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    result = pairs(k, arr)
    print(result)
    fptr.write(str(result) + '\n')
    fptr.close()
