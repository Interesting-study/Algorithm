#https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
def left_diagoanl(arr):
    left = [arr[i][i] for i in range(len(arr))]
    return sum(left)

def right_diagoanl(arr):
    arr_length = len(arr)
    right = [arr[i][arr_length - 1 - i] for i in range(arr_length)]

    return sum(right)


def diagonalDifference(arr):
    # Write your code here
    left_score = left_diagoanl(arr)
    right_score = right_diagoanl(arr)

    return abs(left_score - right_score)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
