# Struggled and finally done
# Took some time , not done using stack , Brute Force only but accepted
# Dated : 25/07/2020
##########################################################################

#!/bin/python3

import math
import os
import random
import re
import sys

def d(st):
    print(f"\n****  {st} ****")

# Complete the largestRectangle function below.
def largestRectangle(h):
    maxi = 0
    for i in range(len(h)):
        count = 0
        for j in range(i+1, len(h)):
            if h[i] > h[j]:
                break
            elif h[i] <= h[j]:
                count += 1
        for k in range(i-1, -1, -1):
            if h[i] > h[k]:
                break
            elif h[i] <= h[k]:
                count += 1
        local_max = (count+1)*h[i]
        if maxi < local_max:
            maxi = local_max
    return maxi


if __name__ == '__main__':

    n = int(input())
    h = list(map(int, input().rstrip().split()))
    result = largestRectangle(h)
    print(result)