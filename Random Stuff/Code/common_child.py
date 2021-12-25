#!/bin/python

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(a,b):
    al = len(a)
    bl = len(b)
    sums = [0]*(al+bl-1)
    for i in range(al):
        for j in range(bl):
            if(a[i]==b[j]):
                sums[i-j+bl-1] +=1
    return(max(sums))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = raw_input()

    s2 = raw_input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
