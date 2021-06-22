class Solution:
    def rearrange(self,arr, n): 
        maxid = n - 1
        minid = 0
        maxel= arr[n-1] + 1
        for i in range(0, n) :
            if i % 2 == 0 :
                arr[i] += (arr[maxid] % maxel) * maxel
                print(arr[i])
                maxid -= 1
            else :
                arr[i] += (arr[minid] % maxel) * maxel
                minid += 1
        for i in range(0, n) :
            arr[i] = arr[i] // maxel
        print(arr[0])
