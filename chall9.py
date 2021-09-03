# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# For example, the square matrix  is shown below:

# 1 2 3
# 4 5 6
# 9 8 9  

def diagonalDifference(arr, n):
    d1 = 0
    d2 = 0
    for i in range (0, n):
        for  j in range (0, n):
            if i == j:
                d1 += arr[i,j]
            if i == n - j - 1:
                d2 += arr[i,j]    
    return abs(d1 - d2);

n = 3
arr = [[11, 2, 4],
       [4 , 5, 6],
       [10, 8, -12]]
            
print(diagonalDifference(arr,n))            