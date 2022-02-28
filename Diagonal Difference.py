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

def diagonalDifference(arr):
    # Write your code here
    left = 0
    right = 0
    
    for i in range(0, len(arr)):
        left = left + arr[i][i]
        right = right + arr[i][len(arr) -1 -i]
            
    return abs(left - right)