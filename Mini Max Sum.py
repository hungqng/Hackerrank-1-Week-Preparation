#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    s = sum(arr)
    
    minResult = s - arr[len(arr) - 1]
    maxResult = s - arr[0]
    
    print(minResult, maxResult)

    # Solution 2
    arr.sort()
    
    minResult = sum(arr[0:4])
    maxResult = sum(arr[1:5])
    
    print(minResult, maxResult)
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
