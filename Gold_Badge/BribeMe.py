#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes1(q):
    nn = len(q)
    ss = 0
    for j in range(nn):
        diff = q[j]-(j+1)
        print(j+1, q[j], " => ", diff)
        if diff > 0:
            ss = ss + diff
            print("ss", ss)
        if diff > 2:
            print("Too chaotic")
            return()
    print(ss)




if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        q = list(map(int, input().rstrip().split()))
        print("\n")
        minimumBribes(q)
