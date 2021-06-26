from collections import deque
class Solution:
    def max_of_subarrays(self,arr,n,k):
        q=deque()
        for i in range(k):
            while q and arr[i]>=arr[q[-1]]:
                q.pop()
            q.append(i)
        l=[]
        for i in range(k,n):
            l.append(arr[q[0]])
            while q and q[0]<=i-k:
                q.popleft()
            while q and arr[i]>=arr[q[-1]]:
                q.pop()
            q.append(i)
        l.append(arr[q[0]])
        return l
