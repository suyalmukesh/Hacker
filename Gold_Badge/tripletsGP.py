#!/bin/python3
# Very easy with Brute force
# Very tough (Not able to solve myself ) for optimizing time complexity
# Need to undersatnd the working code
# -------------------------------------------------------

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets_brute(arr, r):
    n = len(arr)
    count = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[j]/arr[i] == arr[k]/arr[j] == r:
                    print(arr[i], arr[j], arr[k])
                    count += 1
    return count
def countTriplets_2(arr, r):
    n = len(arr)
    lst = []
    count = 0
    for i in range(0, n-1):
        for j in range(i + 1, n):
            if arr[j]/arr[i] == r:
                k = arr[j]*r
                for ele in arr:
                   if ele == k:
                    count += 1
    return count
def countTriplets_3(arr, r):
    n = len(arr)
    lst = []
    count = 0
    for i in range(0, n-1):
        j = arr[i]*r
        if j in arr:
            k = j*r
            j_count = occur(arr, j) - 1
            count = count + occur(arr, k)
            count = count + j_count
    #print(count)
    return count
def occur(arr, k):
    count = 0
    for ele in arr:
        if ele == k:
            count += 1
    return count
def pairs(lst, r, arr):
    count = 0
    for (i, j) in lst :
        k = arr[j]*r
        print(f"k = {k}")
        if k in arr:
            count += 1
    print(count)
    return count
# Working solution , very fast
def countTriplets(arr, r):
    from collections import Counter
    a = Counter(arr)
    b = Counter()
    s = 0
    for i in arr:
        j = i//r
        k = i*r
        # Copied , didn't understand below
        a[i] -= 1
        if b[j] and a[k] and not i % r:
            s += b[j]*a[k]
        b[i] += 1
        # didn't understand till here
    print(s)
    return s


if __name__ == '__main__':
    fptr = open('OUTPUT_PATH', 'w')
    nr = input().rstrip().split()
    n = int(nr[0])
    r = int(nr[1])
    arr = list(map(int, input().rstrip().split()))
    ans = countTriplets(arr, r)
    fptr.write(str(ans) + '\n')
    fptr.close()
