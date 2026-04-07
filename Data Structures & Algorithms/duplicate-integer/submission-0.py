class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dicNums = set(nums)
        print(dicNums)
        if len(dicNums) != len(nums):
            return True
        return False