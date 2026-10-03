class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            num = nums[i]
            search_nums = nums[i+1 :]
            if target - nums[i] in search_nums:
                j = search_nums.index(target - nums[i])
                return [i, j+i+1]
            i += 1
        return []
        