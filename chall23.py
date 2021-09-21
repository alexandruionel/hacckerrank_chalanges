# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

if __name__ == '__main__':
    n = int(input("Please enter a number: "))
    operations = [input("Please enter the operations: ").strip() for _ in range(n)]

    my_list = []

    def insert(index, value):
        my_list.insert(index, value)

    def remove(element):
        my_list.remove(element)

    def append(element):
        my_list.append(element)

    def sort():
        my_list.sort()

    def pop():
        my_list.pop()

    def reverse():
        my_list.reverse()

    for operation in operations:
        command = operation.split()
        if command[0] == 'insert':
                insert(index=int(command[1]), value=int(command[2]))
        elif command[0] == 'remove':
                remove(element=int(command[1]))
        elif command[0] == 'append':
                append(element=int(command[1]))
        elif command[0] == 'sort':
                sort()
        elif command[0] == 'pop':
                pop()
        elif command[0] == 'reverse':
                reverse()
        elif command[0] == 'print':
                print(my_list) 

    