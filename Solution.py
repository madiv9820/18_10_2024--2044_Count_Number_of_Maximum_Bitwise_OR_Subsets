from typing import List
from functools import reduce

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Calculate the maximum OR value that can be obtained from all subsets
        max_or = reduce(lambda x, y: x | y, nums)

        # Helper function to count subsets that achieve the max OR value
        def count_Subsets(index: int = 0, current_or: int = 0) -> int:
            # Base case: if we've considered all elements
            if index == len(nums):
                # Return 1 if the current OR matches the max OR, otherwise return 0
                return 1 if current_or == max_or else 0
            
            # Choice 1: Exclude the current number and move to the next
            choice1 = count_Subsets(index + 1, current_or)
            # Choice 2: Include the current number and move to the next
            choice2 = count_Subsets(index + 1, current_or | nums[index])

            # Return the total count from both choices
            return choice1 + choice2
        
        # Start counting subsets from the first index and initial OR of 0
        return count_Subsets()

# Time Complexity: O(2^n) where n is the length of nums, as we explore all subsets.
# Space Complexity: O(n) for the recursion stack in the worst case.