#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    # Write your code here
    # Starting with no fuel
    position = 0
    fuel = 0
    
    for i in range(len(petrolpumps)):
        # petrolpumps[i][0] is petrol value
        # petrolpumps[i][1] is next pump distance
        # Fuel is whatever amount left at the next distination
        fuel += petrolpumps[i][0] - petrolpumps[i][1]
        if fuel < 0:
            # Go to the next pump
            position = i + 1
            fuel = 0
    return position

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()