Minimum Operation
-----------------------------------------------
To solve the problem of calculating the fewest number of operations needed to result in exactly n 'H' characters in a file, given that the text editor can only execute two operations: Copy All and Paste, you can follow a strategy that minimizes the number of paste operations by maximizing the use of the Copy All operation. This approach is based on the observation that copying all characters and then pasting them is more efficient than pasting a single character multiple times.

Algorithm:
-> Define a function minOperation(n: int) -> int which takes an integer 'n as an input and returns an integer representing the minimum number of operations needed.
-> Check if n is less than or equal to one, if so, return 0.
-> Initialize 'mini_operation' to 0 to keep track of the total number of operations
-> initialize 'current_len' to 1 representing the current length of the string which initially contains one H characters.
-> Enter a loop that continues until the current length of string is less than n.
-> Wthin the loop, check if 'n' is divisible by 'current_len'.If it is, perform the copy all operation(by incrementing mini_operation by 1) and double the length string by doubling current_length.
-> If n is not divisible by current_len, increment current_len by its current value (i.e., perform a paste operation by appending the current string to itself). Increment min_operations by 1 to account for the paste operation.

-> Return min_operations, representing the total number of operations performed to achieve

Main Function:
#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))