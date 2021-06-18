class Solution:
    def MissingNumber(self,array,n):
        ls=[i for i in range(1,n+1)]
        ls=set(ls)
        ar=set(array)
        return (ls^ar).pop()
#  efficient approach findig sum of first  natural numbers
   total_sum=(n+1)*(n)//2
   return total_sum-sum(array)
