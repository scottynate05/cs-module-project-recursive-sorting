# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements

    # initialize the two pointers for each list
    left = 0
    right = 0
    merged_arr = []
    # traverse the lists
    while left < len(arrA) and right < len(arrB):
        if arrA[left] < arrB[right]:
            merged_arr.append(arrA[left])
            left += 1
        else:
            merged_arr.append(arrB[right])
            right += 1
    # now add the elements to the merged_arr
    while left < len(arrA):
        merged_arr.append(arrA[left])
        left += 1
    while right < len(arrB):
        merged_arr.append(arrB[right])
        right += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # base case is when len(arr) == 1
    if len(arr) > 1:
        left = merge_sort(arr[:len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        # merge the left and right arrays
        arr = merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here

