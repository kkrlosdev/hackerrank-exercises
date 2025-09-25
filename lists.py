"""
Consider a list (list = []). You can perform the following commands:

    insert i e: Insert integer e at position i.
    print: Print the list.
    remove e: Delete the first occurrence of integer e.
    append e: Insert integer e at the end of the list.
    sort: Sort the list.
    pop: Pop the last element from the list.
    reverse: Reverse the list.

Initialize your list and read in the value of followed by lines of commands where each command will be of the types listed above.
Iterate through each command in order and perform the corresponding operation on your list. 
"""

if __name__ == '__main__':
    N = int(input())

    arr = []
    for _ in range(N):
        args = input().split()
        command = args[0]
        args = args[1:]
        
        match command:
            case 'insert':
                arr.insert(int(args[0]), int(args[1]))
            case 'print':
                print(arr)
            case 'remove':
                arr.remove(int(args[0]))
            case 'append':
                arr.append(int(args[0]))
            case 'sort':
                arr.sort()
            case 'pop':
                arr.pop()
            case 'reverse':
                arr.reverse()
