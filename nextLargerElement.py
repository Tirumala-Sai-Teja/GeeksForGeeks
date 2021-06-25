class Solution:
    def nextLargerElement(self,arr,n):
        res=[]
        d=[]
        for i in range(n-1,-1,-1):
            #print(arr[i])
            while len(d)>=0:
                if len(d)==0:
                    res.append(-1)
                    d.append(arr[i])
                    #print(d,arr[i],1)
                    break
                else:
                    if arr[i]>=d[-1]:
                        #print(d,arr[i],2)
                        d.pop()
                    else:
                        #print(d,arr[i],3)
                        res.append(d[-1])
                        d.append(arr[i])
                        break
        return res[::-1]
        
