#!/bin/python3

import math
import os
import random
import re
import sys
import functools
#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#
MOD=10**9+7
@functools.lru_cache(None)
def one_row(n): # ways to tile a single row with blocks of width 4,3,2,1
    dp=[0]*max(n+1,5)
    dp[0] = 1
    for i in range(1,n+1):
        sum_=0
        for j in range(1,4+1):
            sum_+=dp[i-j]
        dp[i] = sum_
    return dp[n]
def all_possibilities(n, m):
    return one_row(m)**n

def legoBlocks(n, m):
    # Write your code here
    if m == 1: return 1
    all_poss = all_possibilities(n,m) % MOD
    # print(f"all_poss {all_poss}")
    broken = 0
    for i in range(1, m):
        broken+=(legoBlocks(n,i)*all_possibilities(n,m-i)) 
    return (all_poss-broken) % MOD

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
