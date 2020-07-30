# Understand again
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#
#
#


import math
import os
import random
import re
import sys


def dynamicArray(n, queries):
    lastNumber = 0
    seqList = []
    for i in range(n):
        seqList.append([])
    res = []
    for k, x, y in queries:
        index = (x ^ lastNumber) % n
        if k == 1:
            seqList[index].append(y)
            #print(seqList)
        else:
            size = len(seqList[index])
            #print(seqList)
            #print(size)
            lastNumber = seqList[index][y % size]
            #print(lastNumber)
            res.append(lastNumber)
    return res

def dynamicArray2(n, queries):
    # Write your code here
    lastanswer = 0
    s0, s1 = [], []
    nn = len(queries)
    print("nn", nn)
    result = []
    for i in range(nn):
         q = queries[i][0]
         x = queries[i][1]
         y = queries[i][2]

         seq = 0
         #print("i,q,x,y", i, q, x, y)

         if q == 1:
            print(f"Query {i}" , end = " ")
            print("i,q,x,y", i, q, x, y)
            seq = (x ^ y) % 2

            lastanswer = y

         elif q == 2:
            print(f"Query {i}",end = " ")
            print("i,q,x,y", i, q, x, y)
            seq = (x ^ y) % 2
            if (i > 0):
              lastanswer = queries[i - 1][2]
            else:
              lastanswer = 0
            print(lastanswer)
            result.append(lastanswer)

    return result


if __name__ == '__main__':
    fptr = open('DYNAMIC_ARRAY', 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    result = dynamicArray(n, queries)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
