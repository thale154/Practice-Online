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
    # Sort the array in ascending order
    arr.sort()
    
    # Calculate the minimum sum of the first four elements
    min_sum = sum(arr[:4])
    
    # Calculate the maximum sum of the first four elements
    max_sum = sum(arr[-4:])
    
    # Print the minimum and maximum sums as space-separated integers on one line
    print(min_sum, max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
