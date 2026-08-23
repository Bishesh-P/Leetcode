class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        #Creating Hash table 
        for i in range(n):
            numMap[nums[i]] = i

        # Finding Complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i :#not to have same element twice
                return [i,numMap[complement]]
        return [] #no solution found