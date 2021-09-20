# Task
# Given  names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. 
# You will then be given an unknown number of names to query your phone book for. For each  queried, print the associated entry from your phone book on a new line in the form name=phoneNumber;
# if an entry for  is not found, print Not found instead.

# Note: Your phone book should be a Dictionary/Map/HashMap data structure.

n=int(input())

# initialize a phonebook dictionary object
phoneBook= {}

# checking input data

for i in range(n):
     k, v = input().strip().split()
     phoneBook[k]=v
     
# define a query function

def query(k):
     v= phoneBook[k]
     print(k+"="+v)
     return

# checking input query

for i in range(0, n+1):
     k= input().strip()
     try:
          query(k)
     except:
          print("Not found")