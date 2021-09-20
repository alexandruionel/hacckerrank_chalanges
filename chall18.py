# Task
# Given  names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. 
# You will then be given an unknown number of names to query your phone book for. For each  queried, print the associated entry from your phone book on a new line in the form name=phoneNumber;
# if an entry for  is not found, print Not found instead.

# Note: Your phone book should be a Dictionary/Map/HashMap data structure.

# n=int(input())
# for i in range(1,n):
#      i=str(input())+" "+str(input())
# dict()
# i.update(dict)
# print(dict)
# # for k, v in dict.items(i):
# #     if k in range(dict):
# #         print(i)
#     else:
#         print("Not Found")    

tuple_len = int(input())
a = tuple(map(int, input().split(' ')))
print (hash(a))