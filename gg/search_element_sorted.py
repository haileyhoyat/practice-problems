#https://practice.geeksforgeeks.org/problems/who-will-win-1587115621/1?page=1&difficulty[]=-1&sortBy=submissions

def searchInSorted(self,arr, N, K):
  #Your code here
  if arr.count(K):
      return 1
  else:
      return -1
