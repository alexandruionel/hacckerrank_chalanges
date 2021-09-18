# Task
# Given a string,s , of length n that is indexed from  0to n-1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).

# Note:  is considered to be an even index.

def string(s):
    result_even = ''
    result_odd = ''
    for i in range(len(s)):
        if i % 2 == 0:
            result_even += s[i]
        else:
            result_odd += s[i]
    print(result_even + ' ' + result_odd)

if __name__ == '__main__':
    for i in range(int(input())):
        string(input())           