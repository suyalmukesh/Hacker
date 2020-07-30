# A 6x6 matrix , find the hourglass maximum sum 
# #####################################################
import os
import math
import random
import re
import sys
# Complete the hourglassSum function below.
def hour_glass_sum(array):
    all_sum = []
    for i in range(len(array) - 2):
        for j in range(len(array) - 2):
            hourglass_sum = 0
            hourglass_sum = hourglass_sum + array[i][j] + array[i][j + 1] + array[i][j + 2]
            hourglass_sum = hourglass_sum + array[i + 1][j + 1]
            hourglass_sum = hourglass_sum + array[i + 2][j] + array[i + 2][j + 1] + array[i + 2][j + 2]
            print(hourglass_sum)
            all_sum.append(hourglass_sum)
    return max(all_sum)


if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = hour_glass_sum(arr)
    print(result)
