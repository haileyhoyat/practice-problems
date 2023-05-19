#https://practice.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1?page=1&difficulty[]=-1&sortBy=submissions

'''
Given two arrays A and B of equal size N, the task is to find if given arrays are equal or not. 
Two arrays are said to be equal if both of them contain same set of elements, arrangements (or permutation) of elements may be different though.
Note : If there are repetitions, then counts of repeated elements must also be same for two array to be equal.
'''
def check(A, B):

    #sort() works because sort puts all elements in ascending order, duplicates will also be put in order
    #if there are duplicates in A, duplicates will show up in B in the same index positions as A
    A.sort()
    B.sort()
    
    return True if A==B else False

    '''
    for i in set(A):
        if A.count(i) == B.count(i):
            continue
        else:
            return False
    return True
    '''

    '''
    for i in A:
        if A.count(i) == B.count(i):
            continue
        else:
            return False
    return True   
    '''

if __name__ == '__main__':
    A= [1,2,5,4,0]
    B= [2,4,5,0,1]
    C = [1,2,5]
    D = [2,4,15] 
    E = [3,3]
    F = [2,2]   
    print(check(E,F))
