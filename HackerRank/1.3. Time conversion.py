#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# using datetime module
from datetime import datetime

def timeConversion(s):
    # Write your code here
    in_time = datetime.strptime(s, "%I:%M:%S%p")
    out_time = datetime.strftime(in_time, "%H:%M:%S")
    return out_time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
