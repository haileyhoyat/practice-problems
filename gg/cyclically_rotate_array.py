#https://practice.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1?page=1&difficulty[]=-1&sortBy=submissions

#when rotate clockwise (to the right), use negative numbers
#when rotate counterclockwise (to the left), use positive numbers

#slice method
#get slice starting at n stops from end of the array to end of array --> [5]
#get slice starting at beginning of array to n stops from end of the array --> [1,2,3,4]
#combine two slices together 
def rotate(a, n):

    return a[n:]+a[:n]

#pop method
#obtain last element of arr
#insert element at beginning of arr (all other elements are shifted to the right)
def rotate2(arr, n):
    a=arr.pop()
    arr.insert(0,a)
    return arr

#deque from collections module
def deque(arr,n):
    pass

if __name__ == '__main__':

    a = [1,2,3,4,5]

    b = [9, 8, 7, 6, 4, 2, 1, 3]

    print(rotate(a, -2))
    print(rotate(b, -1))