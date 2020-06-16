# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # base case
    if end >= start:
        # calulate the mid
        mid = (start + end) // 2
        # if the target and the mid are the same
        if arr[mid] == target:
            # return the mid
            return mid
        # if the target is less than the mid
        elif arr[mid] > target:
            # recursively searcb for the target using the first half of the array
            return binary_search(arr, target, start, mid - 1)
        else:
            # recursively search for the target using the last half of the array
            return binary_search(arr, target, mid + 1, end)
    else:
        # return negative -1 AKA not found
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
