class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dicNums = set(nums)
        if len(dicNums) != len(nums):
            return True
        return False