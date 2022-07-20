#!/bin/python3

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

    # Straight forward O(n) solution (fastest possible) - iterate over the whole array once (hence the O(n) complexity), accumulate number of +, - and 0 integers and print respective ratios.
    
    no_positive = 0
    no_negative = 0
    no_zero = 0
    total = 0
    
    for x in arr:
        total += 1
        if x > 0:
            no_positive += 1
        elif x == 0:
            no_zero += 1
        else:
            no_negative += 1
            
    print('{:.6f}'.format(no_positive/total))
    print('{:.6f}'.format(no_negative/total))
    print('{:.6f}'.format(no_zero/total))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
