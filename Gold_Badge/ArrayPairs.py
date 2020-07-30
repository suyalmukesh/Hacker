#!/bin/python3
# Array Pairs
# Working with Brute Force but Time complexity is worst
# The program rejected because of time limit
# This is going to take Time ..
# LEARNING LOGIC OPPORTUNITY
# Keep patience and keep on improving
# B E S T  O F  L U C K
# ---------------------------------------------------
import math
import os
import random
import re
import sys
# Complete the solve function below.
def solve(ar):
    count = 0
    for i in range(0, len(ar) - 1):
        for j in range(i + 1, len(ar)):
            prod = ar[i] * ar[j]
            Max = findMax(i, j, ar)
            if prod <= Max:
                count += 1
    return count
# ------------------------------------- ##
def solve_1(arr):
    arr2 = arr
    count = 0
    probable_j = []
    j_list = []
    #arr = sorted(arr)


    print(j_list)
    return count
# -------------------------------------- ##
def findMax(i, j, arr):
    if i < j:

        maximum = -1
        for m in range(i, j+1):
            maximum = max(maximum, arr[m])
        return maximum
    return -1

def findPairs(arr):
    arr = [1, 2, 3, 4, 5]
    for i in range(0, len(arr)):
        j = i+1


if __name__ == '__main__':
    fptr = open('Array Pairs', 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = solve(arr)
    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
