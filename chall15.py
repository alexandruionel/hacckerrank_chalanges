# Task
# Given an integer,n , print its first 10 multiples. Each multiple n*i (where )1<=i<=10 should be printed on a new line in the form: n x i = result.
# The printout should look like this:

# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# 3 x 5 = 15
# 3 x 6 = 18
# 3 x 7 = 21
# 3 x 8 = 24
# 3 x 9 = 27
# 3 x 10 = 30

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    for i in range(1,11):
        r = n*i
        print(r)
        