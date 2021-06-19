class Solution:
    def subArraySum(self,arr, n, s): 
      
        su=0
        st=0
        end=n
        for i in range(n):
          
           su=arr[i]
           j=i+1
           while(j<=n):
             
                if su==s:
                   return [i+1,j]
                if su>s or j==n:
                    break
                su+=arr[j]
                j+=1
        return [-1]
