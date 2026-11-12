class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            needed = target - num
            # needed = 6
            # seen{4, 0,  5, 1, }
            if needed in seen:
                #           0, 2
                return [seen[needed], i]
            seen[num] = i