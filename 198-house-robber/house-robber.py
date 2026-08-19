class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<2:  # only one element return itself
            return nums[0]
        loot = nums # loot amount is stored in loot array

        loot[0]=nums[0]
        loot[1]=max(nums[0],nums[1]) #for first two houses 

        for i in range(2,len(nums)):
            loot[i] = max(loot[i-2]+loot[i],loot[i-1])

        return loot[len(nums)-1]

        