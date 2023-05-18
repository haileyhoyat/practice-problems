#https://practice.geeksforgeeks.org/problems/reverse-array-in-groups0255/1?page=1&difficulty[]=-1&sortBy=submissions

#in-place means you cant allocate a new array, must only use the given array in the function

def reverseInGroups(a, k):
    # code here
    i=0
    while i<len(a):
        a[i:i+k]=a[i:i+k][::-1]
        i=i+k

    return a

if __name__ == '__main__':
    #K = size of sub-array
    K = 4
    arr = [1,2,3,4,5,6,7,8,9,10,11]
    print(reverseInGroups(arr,K))

"""

get subarray of size k and step backwards in the subarray
a[i:i+k][::-1]
-->    
[4,3,2,1]
[8,7,6,5]
[11,10,9]

replace subarray with reverse subarray
a[i:i+k]
-->
[1,2,3,4]
[5,6,7,8]
[9,10,11]
"""
