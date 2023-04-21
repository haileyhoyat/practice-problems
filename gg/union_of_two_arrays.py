#https://practice.geeksforgeeks.org/problems/union-of-two-arrays3538/1?page=1&difficulty[]=-1&sortBy=submissions

def doUnion(a,n,b,m):
    
    #combine lists
    #turn combined list[] into set to get unique elements from both original lists
    #get length of set{}
    
    return len(set(a+b))

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    b = [1, 2, 3]
    c = [85, 25, 1, 32, 54, 6]
    d = [85,2]

    n = 5
    m = 3
    o = 6
    p = 2

    print(doUnion(a,n,b,m))
    print(doUnion(c, o, d, p))