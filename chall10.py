# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.


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
  positive = sum(x > 0 for x in arr) / len(arr)
  negative = sum(x < 0 for x in arr) / len(arr)
  zero = sum(x == 0 for x in arr) / len(arr)
    
  print(positive, negative, zero, sep="\n")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
