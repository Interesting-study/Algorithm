# !/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Write your code here
    a_dic = defaultdict(int)

    for c in a:
        a_dic[c] += 1
    print(a_dic)

    for c in b:
        a_dic[c] -= 1

    print(a_dic)

    return sum(abs(x) for x in a_dic.values() if x)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
