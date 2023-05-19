
#https://practice.geeksforgeeks.org/problems/find-triplets-with-zero-sum/1?page=1&difficulty[]=-1&sortBy=submissions

from itertools import permutations

#Function to find triplets with zero sum.    
def findTriplets(arr, n):
    #code here
    perms = list(permutations(arr,3))
    for i in perms:
        if sum(i) == 0:
            return True
    return False
    #print(perms)

if __name__ == '__main__':

    n = 5 
    arr = [0, -1, 2, -3, 1]
    print(findTriplets(arr,n))
    #True

    n1 = 3 
    arr1 = [1, 2, 3]
    print(findTriplets(arr1,n1))
    #False