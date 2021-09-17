# Task
# Given an integer,n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n  is even and greater than 20, print Not Weird



import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    
    if (N % 2!=0) or ((N%2==0) and N in range(6,21)):
        print("Weird")
    else:
        print("Not Weird")    

# ONE LINE

 # print("Weird" if (N%2!=0) or (N%2==0 and N in range (6,21))else print ("Not Weird"))    
        