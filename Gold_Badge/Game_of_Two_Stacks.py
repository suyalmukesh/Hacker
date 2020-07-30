# Need to understand this
# Initial solution worked but failed in Time constraints
# Need to analyse
# Dated : 24/07/2020
##############################################

#!/bin/python3

import os
import sys

#
# Complete the twoStacks function below.
#
# Need to understand this
def twoStacks(x, a, b):
    s = 0
    i = 0
    j = 0
    while i < len(a) and s+a[i] <= x:
        s += a[i]
        i += 1
    c = i
    while j < len(b) and i >= 0:
        s += b[j]
        j += 1
        while s > x and i > 0:
            i -= 1
            s -= a[i]
        if s <= x and i+j > c:
            c = i+j
    return c

def twoStacks2(x, a, b):
    sum, count = 0, 0
    while sum < x:
        if a and b:
            continue
        if a[0] == b[0]:
            sum = sum + a[0]
            a.pop(0)
            count += 1
        elif a[0] < b[0]:
            sum = sum + a[0]
            a.pop(0)
            count += 1
        else:
            sum = sum + b[0]
            b.pop(0)
            count += 1
    return count - 1


if __name__ == '__main__':
    g = int(input())
    for g_itr in range(g):
        nmx = input().split()
        n = int(nmx[0])
        m = int(nmx[1])
        x = int(nmx[2])
        a = list(map(int, input().rstrip().split()))
        b = list(map(int, input().rstrip().split()))
        result = twoStacks(x, a, b)
        print(result)


