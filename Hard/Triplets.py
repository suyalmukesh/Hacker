#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(d):
    # Brute Force O(n3) ... Should not be used
    lst = []
    count = 0
    d = sorted(d)
    for i in range(len(d)-2):
        for j in range(i+1, len(d)-1):
            for k in range(j+1, len(d)):
                if (i < j < k) and (d[i] < d[j] < d[k]):
                    lst.append((d[i], d[j], d[k]))
    for (i, j, k) in set(lst):
        if i < j < k:
            count += 1
            print(i, j, k)
    return count
# -------------  #  --------------  #  ----------------- #




if __name__ == '__main__':
    fptr = open('OUTPUT/Triplets', 'w')
    d_count = int(input())
    d = list(map(int, input().rstrip().split()))
    result = solve(d)
    fptr.write(str(result) + '\n')
    fptr.close()
