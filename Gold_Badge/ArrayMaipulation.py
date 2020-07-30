#!/bin/python3
# Here we need to manipulate the array by some queries
# Easy with Brute force but compexity will be high and thus rejected
# used prefix-array sum to improve the complexity
# Done : 13/07/2020
# ---------------------------------------------------- #
import math
import os
import random
import re
import sys
def p(st):
    print("\n*** ", st, " ****")
# Complete the arrayManipulation function below.
def arrayManipulation_done(nn, queries):
    # Brute_force : Complexity n*m : Improvement required
    x = [0] * nn
    q = len(queries)
    for i in range(q):
        start  = queries[i][0]
        end    = queries[i][1]
        value  = queries[i][2]
        for j in range(start-1, end):
            x[j] = x[j] + value
    return max(x)

def arrayManipulation(nn, queries):
    x = [0] * (nn+1)
    q = len(queries)
    p(f"length of array {q} ")
    for i in range(q):
        start = queries[i][0]
        end   = queries[i][1]
        value = queries[i][2]
        print("start:end", start,end)
        x[start-1] = x[start-1] + value
        x[end] = x[end] - value
        print(i, ":", x)
    return maxi(x)
def maxi(a):
    p("Inside prefix sum")
    max_element = 0
    sum = 0
    for i in range(0, len(a)):
        sum = sum + a[i]
        max_element = max(max_element, sum)
        print("i : max_element : sum : array ", i, max_element, sum, a)
    return max_element


if __name__ == '__main__':
    OUTPUT_PATH = "C:\\Users\\C58365A\\Desktop\\out"
    fptr = open('OUTPUT_PATH', 'w')
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    result1 = arrayManipulation(n, queries)
    result2 = arrayManipulation_done(n, queries)
    print(result1)
    print(result2)
    fptr.write(str(result1) + '\n')
    fptr.close()
