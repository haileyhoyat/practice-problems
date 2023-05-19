def find(arr,n,x):
    # code here
    if (x in arr):
        first_index = min(index for index, item in enumerate(arr) if item == x)
        last_index = max(index for index, item in enumerate(arr) if item == x)
    
        return first_index, last_index
    else:

        return -1,-1

'''
find index of first occurence 
first_index = arr.index(x)
'''

'''
find index of last occurence 
rev_arr = arr.reverse()
rev_arr.index(x)
last_index = (len(arr)-index-1)
'''


if __name__ == '__main__':

    n=9 
    x=5
    arr = [1, 3, 5, 5, 5, 5, 67, 123, 125]
    #(2,5)
    print(find(arr,n,x))

    n1=6
    x1=7
    arr1 = [3, 2, 1, 56, 1000, 167]
    print(find(arr1,n1,x1))
    