#!/bin/python3
import math
import os
import random
import re
import sys

import statistics
#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    # Write your code here
    arr.sort()
    
    #return statistics.median(arr)
    
    # Solution 2
    # if number of elements in the array is odd
    if  len(arr) % 2 != 0:
        # Converting to integer to remove the decimal of the odd number
        median = arr[int(len(arr)/2)]
    else:
        median = (arr[(int(len(arr)/2)) -1] + arr[(int(len(arr)/2))]) / 2
    return median
    