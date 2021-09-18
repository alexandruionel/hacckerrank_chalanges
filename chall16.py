# Task
# Given a string,s , of length n that is indexed from  0to n-1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).

# Note:  is considered to be an even index.


t = int(input())
i= str(input())
for i in range(0, t):
    n = len(i)
    index = 0
    for index in range(0,i-1):
        for c in range (i):
            if c%2==0:
                print(c," ")
            else:
                print(" ",c) 
               