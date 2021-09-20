# Given the names and grades for each student in a class of n students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

if __name__ == '__main__':
    
    l= [[input(), float(input())] for _ in range(int(input()))]
sh = sorted(list(set([m for name, m in l])))[1]
print('\n'.join([a for a,b in sorted(l) if b == sh]))