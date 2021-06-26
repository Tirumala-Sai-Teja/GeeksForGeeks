#User function Template for python3

class stack:
    def __init__(self):
        self.s=[]
        self.minEle=None

    def push(self,x):
        if len(self.s)==0:
            self.s.append(x)
            self.minEle=x
        else:
            if x<self.minEle:
                self.s.append((2*x)-self.minEle)
                self.minEle=x
            else:
                self.s.append(x)

    def pop(self):
        if len(self.s)==0:
            return -1
        else:
            y=self.s.pop()
            
            if y<self.minEle:
                p=self.minEle
                self.minEle=2*self.minEle-y
                return p
            else:
                return y
    def getMin(self):
        if len(self.s)==0:
            return -1
        else:
            return self.minEle
