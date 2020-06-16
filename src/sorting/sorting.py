# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # if there is an array with more than 1 element
    if len(arr) > 1:
        # calculate the mid
        mid = len(arr) //2
        # set new array to all elements from the 0-mid
        newarr1 = arr[:mid]
        # set new array to all elements from the mid - end
        newarr2 = arr[mid:]
        # preform recursion on both new arrays
        merge_sort(newarr1)
        merge_sort(newarr2)
        # set variable for new array 1
        na1 = 0
        # set variable for new array 2
        na2 = 0
        # set variable for the original array
        oarr = 0
        while na1 < len(newarr1) and na2 < len(newarr2):
            if newarr1[na1] < newarr2[na2]:
                arr[oarr] = newarr1[na1]
                na1 = na1 + 1
            else:
                arr[oarr] = newarr2[na2]
                na2 = na2 + 1
            oarr = oarr + 1

        while na1 < len(newarr1):
            arr[oarr] = newarr1[na1]
            na1 = na1 + 1
            oarr = oarr + 1
        
        while na2 < len(newarr2):
            arr[oarr] = newarr2[na2]
            na2 = na2 + 1
            oarr = oarr + 1
    return arr

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here

    pass