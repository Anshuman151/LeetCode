class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = []
        i=0
        while i < len(nums):
            if nums[i] not in a:
                a.append(nums[i])
            elif nums[i] in a:
                a.remove(nums[i])
            i+=1
        return a[0]
            