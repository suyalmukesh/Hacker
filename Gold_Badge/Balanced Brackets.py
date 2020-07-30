# Worked perfectly fine , Passed
# Dated : 23/07/2020
# Stack concept should be good
##########################################

#!/bin/python3

import math
import os
import random
import re
import sys

key = {
    "]": "[",
    "}": "{",
    ")": "("
}

def isBalanced(s):
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
        elif i in ('[', '{', '('):
            stack.append(i)
        elif i in ('}', ']', ')'):
            if stack and stack[-1] == key.get(i):
                stack.pop()
        else:
            return "NO"
    if not stack:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open('Balanced_Brackets', 'w')
    t = int(input())
    for t_itr in range(t):
        s = input()
        result = isBalanced(s)
        print(result)
    fptr.close()
