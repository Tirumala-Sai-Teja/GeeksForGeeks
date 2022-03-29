#User function Template for python3
'''this logic helps to find the number which is repeated odd number of times in an array'''
class Solution:
    def findSingle(self, N, arr):
        x=arr[0]
        for i in range(1,len(arr)):
            x^=arr[i]
        return x

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        
        ob = Solution()
        print(ob.findSingle(N, arr))

# } Driver Code Ends
