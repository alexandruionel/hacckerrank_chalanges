# https://www.hackerrank.com/challenges/list-comprehensions/problem





if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    print([[i, j,k] for i in [x,y,z] for j in [x,y,z] for k in [x,y,z]])            
    
    