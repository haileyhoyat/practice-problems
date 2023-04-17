#https://practice.geeksforgeeks.org/problems/binary-search-1587115620/1?page=1&difficulty[]=-1&sortBy=submissions

def BinarySearchIterative(arr, left, right, x):
    while left <= right:
        mid = left + (right - left)//2

        if arr[mid] == x:
            return mid
        
        elif arr[mid] < x:
            left = mid + 1

        else:
            right = mid - 1

    return -1

def BinarySearchRecursive(arr, left, right, x):
    if left <= right:
        mid = left + (right-left) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return BinarySearchRecursive(arr, mid+1, right, x)
        else:
            return BinarySearchRecursive(arr, left, mid-1, x)
    else:
        return -1

if __name__ == '__main__':
    
    arr = [2,3,4,10,40]
    x = 5

    resultIterative = BinarySearchIterative(arr, 0, len(arr)-1, x)
    if resultIterative != -1:
        print("Element is present at index", resultIterative)
    else:
        print("Element is not present in the array")

    resultRecursive = BinarySearchRecursive(arr, 0, len(arr)-1, x)
    if resultRecursive != -1:
        print("Element is present at index", resultRecursive)
    else:
        print("Element is not present in the array")

"""
Binary search is searching alogrotihm used in a sorted array by repeadely cutting the search interval in half. 

Find the index of a given element. 

Reduces time complexity to O(log N).

Data structure must:
    1) be sorted
    2) access to each element of data structure takes constant time. 

Constant time means the algorithm takes the same amount of time no matter the input size.
Ex: The time it takes to access index[i] is always the same no matter how large the array is. 

Can implement binary search through iterative or recursive method.
Iterative means some part of the function loops to repeat some part of itself.
Recursive means the function calls itself to repeat the code. 

Calculate mid using: mid = low + (high – low)//2
Here 'low' is the lowest index (usually 0) and 'high' is highest index (usually the last index in the array, aka len(arr[])-1).
Will also see left (low) and right (high) being used. 
(there's a whole reason for this but for now jsut take it for what it is)
"""
