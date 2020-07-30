#!/bin/python3
# Working perfectly
# Easy .. O(n)
# Date : 20/07/2020
# ----------------------- #
import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    count = 0
    prev = ""
    for i in range(0, len(s)):
        current = s[i]
        if current == prev:
            count += 1
        prev = current
    print(count)
    return count


if __name__ == '__main__':
    fptr = open('Alternating_Characters', 'w')
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = alternatingCharacters(s)
        fptr.write(str(result) + '\n')
    fptr.close()
