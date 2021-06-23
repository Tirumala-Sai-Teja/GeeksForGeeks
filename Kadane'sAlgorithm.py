class Solution:
    def maxSubArraySum(self,a,size):
        sm=-99999999
        s1=0
        for i in range(size):
            s1+=a[i]
            if sm<s1:
                sm=s1
            if s1<0:
                s1=0
        
        return(sm)  
