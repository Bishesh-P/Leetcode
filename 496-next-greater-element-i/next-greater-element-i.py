class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for n in nums1:
            index = nums2.index(n)
            greater = -1
            for i in range(index + 1,len(nums2)):
                if nums2[i] > n:
                    greater = nums2[i]
                    break
            ans.append(greater)
        return ans
               
        