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
get the subarray to replace


a[i:i+k] -->
[1,2,3]
[4,5,6]
[7,8,9]
[10,11]

a[i:i+k][::-1] -->     
[3,2,1]
[6,5,4]
[9,8,7]
[11,10]

"""