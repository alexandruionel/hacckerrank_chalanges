# # Given an array,a ,n of  integers, print a 's elements in reverse order as a single line of space-separated numbers.
# Sample Input

# 4
# 1 4 3 2

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    for i in range(len(arr)-1, -1, -1):   
        print (arr[i],end =" ")
            
        