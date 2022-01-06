# User function Template for Python3
class queEntry:
    def __init__(self,v=0,dist=0):
        self.v=v
        self.dist=dist
    
class Solution:
    def minThrow(self, N, arr):
        
        ar=[-1]*30

        for i in range(0,len(arr)-1,2):
            # print(i,i+1)
            ar[arr[i]-1]=arr[i+1]-1
        # print(ar)
        visited=[False]*30
        queue=[]
        visited[0]=True
        queue.append(queEntry(0,0))
        qe=queEntry()
        while queue:
            qe=queue.pop(0)
            v=qe.v
            if v==29:
                break
            j=v+1
            while j<=v+6 and j<30:
                if visited[j] is False:
                    a=queEntry()
                    a.dist=qe.dist+1
                    visited[j]=True
                    a.v=ar[j] if ar[j]!=-1 else j
                    queue.append(a)
                j+=1
        return qe.dist
    
 

#{ 
#  Driver Code Starts
# Initial Template for Python3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(2*N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.minThrow(N, arr))

# } Driver Code Ends

'''
input:
1
8
3 22 5 8 11 26 20 29 17 4 19 7 27 1 21 9 
output:3  '''
