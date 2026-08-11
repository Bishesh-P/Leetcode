class Solution:
    def jump(self, nums: List[int]) -> int:
        totaljumps = 0
        destination = len(nums) -1
        coverage = 0
        lastjumpidx = 0
        if len(nums) == 1:
            return 0
        for i in range(len(nums)):
            coverage = max(coverage,i+nums[i])
            
            if i == lastjumpidx:
                lastjumpidx = coverage
                totaljumps+=1

                if coverage >= destination:
                    return totaljumps

        return totaljumps