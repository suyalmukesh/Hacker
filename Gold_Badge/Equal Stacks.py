#!/bin/python3

import os
import sys
sys.setrecursionlimit(10**6)
#
# Complete the equalStacks function below.
#
def height(a):
    height = 0
    for i in a:
        height = height + i
    return height

# This is working for failing for Time constraints
def equalStacks(h1, h2, h3):
    maximum = -1
    while maximum == -1:
        height1, height2, height3 = height(h1), height(h2), height(h3)
        print(height1, ":", height2, ":", height3)
        if height1 == height2 == height3:
            maximum = height1
        else:
            if max(height1, height2, height3) == height1:
                h1.pop(0)
            elif max(height1, height2, height3) == height2:
                h2.pop(0)
            else:
                h3.pop(0)

    return maximum

# Copied this ... but working like charm
def EqualStacks(h1, h2, h3):
    s1, s2, s3 = map(sum, (h1, h2, h3))
    while h1 and h2 and h3:
        m = min(s1, s2, s3)
        while s1 > m: s1 -= h1.pop(0)
        while s2 > m: s2 -= h2.pop(0)
        while s3 > m: s3 -= h3.pop(0)
        if s1 == s2 == s3: return s1
    return 0

############################################

if __name__ == '__main__':

    n1N2N3 = input().split()
    n1 = int(n1N2N3[0])
    n2 = int(n1N2N3[1])
    n3 = int(n1N2N3[2])
    h1 = list(map(int, input().rstrip().split()))
    h2 = list(map(int, input().rstrip().split()))
    h3 = list(map(int, input().rstrip().split()))
    result2 = EqualStacks(h1, h2, h3)
    print("result2",result2)

    result = equalStacks(h1, h2, h3)
    print("result1",result)

