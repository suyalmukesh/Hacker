import os
import sys

ar = [1, 1, 5, 4, 3, 6, 6, 5, 9, 10]

n = len(ar)
for i in range(n):
    for j in range(n):
        if i < j:
            print(i, j)

