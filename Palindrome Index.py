#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    # Write your code here
    for i,j in enumerate(range(0,len(s)//2),1):
        if s[-i] == s[j]:
            continue
        if s[j:-i]==s[j:-i][::-1]:
            return len(s)-i
        elif s[j+1:-i+1]==s[j+1:-i+1][::-1]:
            return j
        return -1
    return -1

    # Solution 2
    # l = len(s)
    # i = 0
    # j = l-1
    # while i<l:
    #     if s[i]!=s[j]:
    #         break
    #     i+=1
    #     j-=1
    # if i>j: return -1
    # a = i+1
    # b = j
    # while a<j and b>i+1:
    #     if s[a]!=s[b]:
    #         return j
    #     a+=1
    #     b-=1
    # return i


    # if s == s[::-1]:
    #   return -1
    #
    #n = len(s)
    #
    #for i in range(n//2)
    #    if s[i] != s[n-1-i]:
    #       if s[i:n-1-i] == s[i:n-1-i][::-1]:
    #           return n-1-i
    #       elif s[i+1:n-i] == s[i+1:n-i][::-1]:
    #           return i
    #return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()