from collections import deque
class Solution:
    def ispar(self,x):
        d=deque()
        d1={')':'(',']':'[','}':'{'}
        for i in x:
            if i in d1.values():
                d.append(i)
            elif i in d1.keys():
                if len(d)<1:
                    return 0
                p=d.pop()
                if d1[i]!=p:
                    return 0
        return 1 if len(d)==0 else 0
                    
