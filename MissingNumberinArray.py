class Solution:
    def MissingNumber(self,array,n):
        ls=[i for i in range(1,n+1)]
        ls=set(ls)
        ar=set(array)
        return (ls^ar).pop()
