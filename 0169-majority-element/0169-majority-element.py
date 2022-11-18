class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        a = {}
        for i in nums:
            if i not in a:
                a.setdefault(i,1)
            elif i in a:
                a[i]+=1
        for i in a:
            if a[i]>n//2:
                return i