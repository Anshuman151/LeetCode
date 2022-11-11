class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        out = []
        for i in nums:
            out.append(i**2)
        out.sort()
        return out