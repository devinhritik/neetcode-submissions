class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if(len(nums) < 1):
            return 0
        count = 1
        currcount = 1
        for i in range(len(nums)-1):
            val = i
            if(nums[i+1] == nums[i]+1):
                currcount += 1
            elif nums[i+1] == nums[i]:
                continue
            else:
                count = max(count,currcount)
                currcount = 1
        count = max(count,currcount)
        return count 