# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# For example, the square matrix  is shown below:

# 1 2 3
# 4 5 6
# 9 8 9  

def diagonalDifference(arr):
    my_sum1 = 0
    my_sum2 = 0
    for i in range(len(arr)):
        my_sum1 += arr[i][i]
        my_sum2 += arr[i][len(arr)-i-1]
    return abs(my_sum1-my_sum2)