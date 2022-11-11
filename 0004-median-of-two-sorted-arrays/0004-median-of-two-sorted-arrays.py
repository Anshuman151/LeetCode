class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []
        for i in range(len(nums1)):
            arr.append(nums1[i])
        for j in range(len(nums2)):
            arr.append(nums2[j])
        arr.sort()
        if len(arr) % 2 != 0:
            b = int(len(arr)/2 + 0.5)
            return arr[b-1]
        elif len(arr) % 2 == 0:
            b = int(len(arr) / 2)
            return (arr[b-1]+ arr[b])/2