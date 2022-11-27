class Solution:
    def pivotInteger(self, n: int) -> int:
        r = n
        for i in range(1,n+1,1):
            if sum(range(1,r+1)) == sum(range(r,n+1)):
                return r
            r-=1
            if r<1:
                return -1
    
            