#!/bin/python3
#https://www.hackerrank.com/challenges/plus-minus/problem
import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    plus = minus = zero = 0
    length = len(arr)

    for val in arr:
        if val > 0:
            plus += 1
        elif val < 0:
            minus += 1
        else:
            zero += 1

    print('{:.6f}\n{:.6f}\n{:.6f}'.format(plus / length, minus / length, zero / length))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
