#!/bin/python3
# Find the occurance of a string in another string 
# Very easy , but here the complexity is O(n*m)
# TRy to improve the compexity 
# Date : 14/07/2020
# ----------------------------------------------------#
import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    my_list = []
    for i in queries:
        count = 0
        for j in strings:
            if j == i:
                count += 1
        my_list.append(count)
    return my_list


if __name__ == '__main__':
    fptr = open('OUTPUT_PATH', 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)


    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    #fptr.close()

